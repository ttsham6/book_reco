/**
 * ユーザー状態保管クラス
 * ブラウザの情報を操作する
 */
class User {
  // getter/setter
  get = key => {
    return this.getLocalStorage(key);
  };
  set = (key, value) => localStorage.setItem(key, value);

  // ブラウザ情報を取得する
  getLocalStorage = key => {
    const ret = localStorage.getItem(key);
    if (ret) {
      return ret;
    }
    return null;
  };

  // ログイン状態確認
  isLoggedIn = () => {
    return this.get("isLoggedIn") === "true";
  };

  // ログイン処理
  login = async () => {
    this.set("isLoggedIn", true);
    // TODO サーバへログインリクエストを送る。

    return true;
  };

  // ログアウト処理
  logout = async () => {
    if (this.isLoggedIn()) {
      this.set("isLoggedIn", false);
    }
  };
}

export default new User();
