import React, { Fragment, useState, useEffect } from "react";
import SearchView from "../Presentational/SearchView";
import User from "../../Route/User";
/**
 * 書籍検索結果をAjax通信で取得するコンポーネント
 */

export default function SearchJson(props) {
  const [items, setItems] = useState([]);
  const [error, setError] = useState("");
  const [isLoading, changeLoading] = useState(0);
  const { handleGetReco, genre, keyword } = props;

  useEffect(() => {
    // 送信パラメータ作成
    if (keyword !== "") {
      const params = new URLSearchParams();
      const userId = User.get("userId");
      params.append(
        "params",
        JSON.stringify({
          keyword,
          genre,
          userId
        })
      );

      changeLoading(1); // ローディング中

      // request
      fetch("http://127.0.0.1:8000/book_reco/search/", {
        method: "POST",
        mode: "cors",
        body: params
      })
        .then(res => res.json())
        .then(
          result => {
            // 通信成功時
            setItems(result);
            changeLoading(2);
            handleGetReco();
          },
          error => {
            // エラー発生時
            setError(error);
            changeLoading(2);
          }
        );
    }
  }, [keyword]);

  return <SearchView isLoading={isLoading} error={error} items={items} />;
}
