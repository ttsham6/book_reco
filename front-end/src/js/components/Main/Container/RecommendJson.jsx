import React, {
  useState,
  useEffect,
  forwardRef,
  useImperativeHandle,
  Fragment
} from "react";
import RecommendView from "../Presentational/RecommendView";
import User from "../../Route/User";

/**
 * レコメンド結果をAjax通信で取得するコンポーネント
 */
function RecommendJson(props, ref) {
  const [items, setItems] = useState([]);
  const [error, setError] = useState("");
  const [isLoading, changeLoading] = useState(1);
  const [genre, setGenre] = useState("本");

  useImperativeHandle(ref, () => ({
    getNewRecommend: () => {
      // 検索実行後
      sendRequest(false);
    }
  }));

  useEffect(() => {
    // 初期表示
    sendRequest(true);
  }, []);

  const sendRequest = init => {
    // 送信パラメータ作成
    const params = new URLSearchParams();
    const userId = User.get("userId");
    params.append(
      "params",
      JSON.stringify({
        genre,
        init,
        userId
      })
    );

    changeLoading(1); // ローディング中

    // request
    fetch("http://127.0.0.1:8000/book_reco/recommend/", {
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
        },
        error => {
          // エラー発生時
          setError(error);
          changeLoading(2);
        }
      );
  };

  return (
    <Fragment>
      <RecommendView error={error} isLoading={isLoading} items={items} />
    </Fragment>
  );
}

RecommendJson = forwardRef(RecommendJson);
export default RecommendJson;
