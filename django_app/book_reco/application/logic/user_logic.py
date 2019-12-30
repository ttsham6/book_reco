"""
ユーザー管理機能メインロジック
"""
from book_reco.domain.models import UserData


def user_auth(userId, password):
    """
    ユーザー認証を行う

    Parameters
    ----------
    userId : ユーザーID

    password : パスワード

    Returns
    -------
    result : str
        ユーザー認証結果:
            "success":認証成功
            その他：エラーメッセージ

    """
    try:
        passData = UserData.objects.values(
            'password').get(userId=userId)['password']
    except Exception as e:
        print(e)
        return "ユーザーが存在しません"

    if passData != password:
        return "パスワードが一致しません"

    return "success"


def regist_user_info(userId, password):
    """
    ユーザー登録を行う

    Parameters
    ----------
    userId : ユーザーID

    password : パスワード

    Returns
    -------
    result : str
        ユーザー登録結果:
            "success":認証成功
            その他：エラーメッセージ
    """

    # 同一のユーザーIDが存在しないかを確認
    if not _check_userId(userId):
        return "既に同一のユーザーが存在します"

    # ユーザー登録
    try:
        UserData.objects.create(
            userId=userId,
            password=password
        )
    except Exception as e:
        print(e)
        return "ユーザー登録に失敗しました"

    return "success"


def _check_userId(userId):
    """
    同一のユーザーIDが既に登録されていないかを判定する

    Parameters
    ----------
    userId : ユーザーID

    Returns
    -------
    result : boolean
        True : 登録なし
        False : 登録済み
    """

    try:
        count = UserData.objects.filter(userId=userId).count()
        if count > 0:
            return False
    except Exception as e:
        print(e)
        return False

    return True
