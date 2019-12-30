import React, { useState } from "react";
import LoginView from "../Presentational/LoginView";
import User from "../../Route/User";
import { Redirect } from "react-router-dom";
import RegistrationView from "../Presentational/RegistrationView";

/**
 * ログイン画面処理コンポーネント
 */
export default function LoginJson() {
  const [error, setError] = useState("");
  const [isLoading, changeLoading] = useState(0);
  const [type, changeType] = useState("login");

  const sendRequest = (userId, password) => {
    const params = new URLSearchParams();
    params.append(
      "params",
      JSON.stringify({
        userId,
        password,
        type
      })
    );

    changeLoading(1); // ローディング中

    // request
    fetch("http://127.0.0.1:8000/book_reco/login/", {
      method: "POST",
      mode: "cors",
      body: params
    })
      .then(res => res.json())
      .then(
        result => {
          if (result.result === "success") {
            console.log("login");
            console.log(result.result);
            // 通信成功時
            changeLoading(2);
            // ブラウザのログイン情報を「ログイン済み」に変更
            User.login();
            User.set("userId", userId);
            // コンポーネントの情報を変更
          }
        },
        error => {
          // エラー発生時
          setError(error);
          changeLoading(2);
        }
      );
  };

  if (type == "login") {
    // 未ログインの場合
    // ログイン画面を描画
    return (
      <LoginView
        error={error}
        sendRequest={sendRequest}
        isLoading={isLoading}
        changeType={changeType}
      />
    );
  } else if (type == "regist") {
    return (
      <RegistrationView
        sendRequest={sendRequest}
        error={error}
        isLoading={isLoading}
      />
    );
  }
}
