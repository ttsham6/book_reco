"""
クライアントとのデータの受け渡し
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from book_reco.view.serializers import SearchModelSerializer, RecommendModelSerializer
from book_reco.application.logic import search_logic, recommend_logic, user_logic
from rest_framework.decorators import api_view
import json
# import time


# Create your views here.
@csrf_exempt
@api_view(['POST'])
def search_info(request):
    """
    書籍データを検索する
    /search へのリクエストを処理する

    Parameters
    ----------
    request : request
        リクエスト情報

    Returns
    -------
    レスポンス : Json形式の書籍情報

    """

    req_data = json.loads(request.data['params'])

    # search_res = recommend_logic.get_previous_recommend()  # ダミー
    # serializer = RecommendModelSerializer(search_res, many=True)  # ダミー
    # time.sleep(5)  # プログレスバー動作確認用
    try:
        # 実環境
        search_res = search_logic.search_book_info(
            req_data["userId"], req_data["keyword"], req_data["genre"])
        serializer = SearchModelSerializer(search_res, many=True)
        response = JsonResponse(serializer.data, safe=False)
    except Exception as e:
        print(e)
        response = JsonResponse("Error")

    return response


@csrf_exempt
@api_view(['POST'])
def reccomend_info(request):
    """
    ユーザー傾向にマッチした書籍を取得する
    /recommend へのリクエストを処理する

    Parameters
    ----------
    request : request
        リクエスト情報

    Returns
    -------
    レスポンス : Json形式の書籍情報

    """
    req_data = json.loads(request.data["params"])
    isInitial = req_data["init"]
    try:
        if isInitial:
            search_res = recommend_logic.get_previous_recommend(
                req_data["userId"])
            serializer = RecommendModelSerializer(search_res, many=True)
            response = JsonResponse(serializer.data, safe=False)
        else:
            # search_res = recommend_logic.get_previous_recommend()  # ダミー
            search_res = recommend_logic.get_recommend_info(
                req_data["userId"], req_data["genre"])
            serializer = RecommendModelSerializer(search_res, many=True)
            response = JsonResponse(serializer.data, safe=False)
    except Exception as e:
        print(e)
        response = JsonResponse("Error")

    # APIから取得した値をシリアライズ

    # time.sleep(5)  # プログレスバー動作確認用
    print("Recommend!")
    return response


@csrf_exempt
@api_view(['POST'])
def user_info(request):
    """
    ユーザーログイン・ログアウト、登録を管理
    /login へのリクエストを処理する

    Parameters
    ----------
    request : request
        リクエスト情報

    Returns
    -------
    レスポンス : 登録結果

    """

    req_data = json.loads(request.data["params"])
    # req_data = request.data["params"][0]
    if req_data["type"] == "login":
        # ログイン処理
        result = user_logic.user_auth(req_data["userId"], req_data["password"])
    elif req_data["type"] == "regist":
        # ユーザー登録処理
        result = user_logic.regist_user_info(
            req_data["userId"], req_data["password"])
    else:
        # エラー処理
        result = "要求情報が設定されていません。"

    ret = {
        "result": result
    }

    return JsonResponse(ret)
