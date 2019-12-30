import React from "react";
import { Redirect } from "react-router-dom";
import User from "./User";

/**
 * ログイン状態を判定し、ログイン画面かホーム画面にリダイレクトするコンポーネント
 */
export default function Auth(props) {
  // User.logout();
  if (User.isLoggedIn()) {
    // ログイン済み
    return props.children;
  } else {
    // 未ログイン
    return <Redirect to={"/login"} />;
  }
}
