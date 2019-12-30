"""
楽天ブックスAPI
ライブラリ実行用
参考　https://webservice.rakuten.co.jp/api/booksbooksearch/
"""
import json
import os
import time


import requests

RAKUTEN_BOOKS_API_URL = "https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404?"
CWD = os.getcwd()
SOURCE_FILE = 'rakuten_app_info.txt'
GENRE_ID_FILE = 'genre_id_p.json'
search_hits = 8
search_pages = 1
reccomend_hits = 4
reccomend_pages = 1
dataset_hits = 30
dataset_pages = 100

# _____________________________________________________________
# UTIL
# _____________________________________________________________


def read_id():
    """
    設定ファイルからアプリIDを取得

    Returns
    -------
    app_id : str
        アプリケーションID

    """

    id_file = os.path.join(CWD, 'django_app', 'book_reco',
                           'application', 'api', SOURCE_FILE)
    # id_file = os.path.join(CWD, 'book_reco', 'application', 'api', SOURCE_FILE)
    with open(id_file, 'r') as f:
        app_id = f.readline()

    return app_id


def send_request(payload):
    """
    APIへ要求を行う
    """
    # print(time.time())

    url = RAKUTEN_BOOKS_API_URL

    response = requests.get(url, params=payload)
    res_dict = json.loads(response.text)
    time.sleep(1)

    return res_dict


# _____________________________________________________________
# 検索機能用
# _____________________________________________________________


def search_book_info(keyword, genre):
    """

    検索キーワードから書籍情報を取得する

    Parameters
    ------------
    keyword : str
        検索ワード

    genre : str
        ジャンル

    Returns
    ------------
    res_dict : dict
        リクエストに対する書籍データ

    """

    # ジャンル情報を取得
    genreidfile_path = os.path.join(
        CWD, 'django_app', 'book_reco', 'application', 'api', GENRE_ID_FILE)
    with open(genreidfile_path, 'r', encoding='utf-8') as f:
        genre_dict = json.load(f)

    genre_id = str(genre_dict[genre])
    rakuten_id = read_id()

    # 要求情報作成
    payload = {
        'applicationId': rakuten_id,
        'booksGenreId': genre_id,
        'hits': search_hits,
        'page': search_pages,
        'sort': 'sales'
    }

    # キーワード検索を行う場合
    if(keyword is not None):
        payload['keyword'] = keyword

    # 書籍情報取得
    res_dict = send_request(payload)

    return res_dict

# _____________________________________________________________
# レコメンド機能用
# _____________________________________________________________


def search_book_info_by_isbn(isbn):
    """
    ISBNを使用して、書籍情報を検索する

    paramerters
    ------------
    isbn : int
        ISBN

    results
    ------------
    res_list : list
        リクエストに対する書籍データリスト

    """

    rakuten_id = read_id()

    # 要求情報作成
    payload = {
        'applicationId': rakuten_id,
        'isbnjan': isbn,
    }

    # 書籍情報取得
    res_dict = send_request(payload)

    return res_dict

# _____________________________________________________________
# データセット作成機能用
# _____________________________________________________________


def create_imagedataset():
    """
    CSVファイルに保存するデータセットを作成する

    Returns
    ------------
    book_info_list : list[dict]
        データセット用書籍情報
    """

    # データセット用書籍情報取得
    res_list = _get_dataset_info()

    # データ整形
    book_info_list = _reshape_dataset(res_list)

    return book_info_list


def _get_dataset_info():
    """

    データセット用の書籍情報を取得する

    Paramerters
    ------------

    Returns
    ------------
    res_list : list
        リクエストに対する書籍データ

    """

    rakuten_id = read_id()

    res_list = []
    # 指定ページ文リクエストを行う
    for i in range(dataset_pages):
        payload = {
            'applicationId': rakuten_id,
            'booksGenreId': "001",
            'hits': dataset_hits,
            'page': i + 1,
            'sort': 'sales'
        }

        # 書籍情報取得
        res_dict = send_request(payload)
        res_list.append(res_dict)

        print("Request")
        print("No" + str(i))

    return res_list


def _reshape_dataset(res_list):
    """
    階層構造になっている書籍データを整形する

    Paramerters
    ------------
    res_list : list[dict]
        書籍情報（JSON形式）
        APIから取得した整形前のデータ

    Resutls
    ------------
    book_info_list : list[dict]

    """

    book_id = 0

    book_info_list = []

    for book_info in res_list:
        # リクエスト回数文ループ処理
        if('Items' not in book_info):
            break
        items = book_info['Items']

        for item in items:
            # 1回のリクエスト内の書籍情報文回数文ループ処理
            book_id += 1
            book_info = item['Item']
            book_info_list.append(book_info)

    return book_info_list


if __name__ == '__main__':

    keyword = 'python'
    genre = '小説・エッセイ'
    result = search_book_info(keyword, genre)
    time.sleep(1)
    with open('sample_res.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False,
                  indent=4)
    print(result)
    None
