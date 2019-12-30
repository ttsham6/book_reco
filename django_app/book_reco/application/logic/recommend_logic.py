"""
レコメンド機能メインロジック
"""
from book_reco.domain.models import RecommendData, SearchData, DatasetData
from book_reco.application.api import book_api as bookapi
from book_reco.application.recommend import recommend_analysis

user_num = 5  # 平均を算出する件数


def get_previous_recommend(userId):
    """
    初期表示時のおすすめ情報を取得
    前回のレコメンド結果から取得する

    Parameters
    ----------
    userId : str
        ユーザーID

    Returns
    -------
    obj : 前回のレコメンド結果

    """
    obj = list(RecommendData.objects.filter(userId=userId).order_by(
        'id').reverse()[:4])
    return obj


def get_recommend_info(userId, genre):
    """
    おすすめの書籍データを取得する。

    Parameters
    ----------
    userId : str
        ユーザーID

    keyword : str
        検索ワード

    genre : str
        ジャンル名

    Returns
    -------
    obj : 最新の検索結果

    """
    try:
        # データセットをファイルから読み込む
        book_info_list = _input_dataset()

        # ユーザーの傾向情報を生成
        # user_img = _get_user_preference(userId)
        user_img = _get_user_preference_list(userId)

        # ユーザーの傾向と近い書籍を抽出
        sim_dict = recommend_analysis.create_recommend_list(
            book_info_list, user_img)

        # DBへの書き込み処理
        for isbn in sim_dict.keys():

            # search_result = bookapi.search_book_info_by_isbn(isbn)
            reco_item = DatasetData.objects.all().filter(isbn=isbn).last()

            # modelsを通してDBへの書き込みを行う
            RecommendData.objects.create(
                userId=userId,
                genre=genre,
                title=reco_item.title,
                author=reco_item.author,
                itemCaption=reco_item.itemCaption,
                publisherName=reco_item.publisherName,
                salesDate=reco_item.salesDate,
                itemPrice=str(reco_item.itemPrice),
                itemUrl=reco_item.itemUrl,
                imageUrl=reco_item.imageUrl
            )

        # DBから最新の情報を取得
        obj = list(RecommendData.objects.values().order_by(
            'id').reverse()[:len(sim_dict)])
        return obj

    except Exception as e:
        print('表示エラー')
        print(e)


def _input_dataset():
    """
    CSVファイルから書籍情報データセットを取得する

    Parameters
    ----------

    Returns
    -------
    book_info_list : list[dict]
        データセット情報リスト
        isbn : 書籍ISBN、feature : 特徴量ベクトル
    """

    book_info_list = []

    with open('./django_app/feature_dataset.csv', 'r') as f:
        item_list = f.readlines()

    # データを整形する
    for item in item_list:

        row = item.rstrip().split(",")
        # 要素を辞書に格納
        book_info = {}
        book_info["isbn"] = row[0]
        book_info["feature"] = row[1]
        book_info_list.append(book_info)

    return book_info_list


def _get_user_preference(userId):
    """
    ユーザーの傾向を取得する

    Returns
    -------
    user_img : stt
        ユーザーの直近の画像URL
    """

    # ユーザーの好む書籍情報を生成
    # TODO: 複数件情報を合成
    user_item_obj = SearchData.objects.filter(userId=userId).latest('id')
    user_img = user_item_obj.imageUrl
    return user_img


def _get_user_preference_list(userId):
    """
    ユーザーの検索履歴から画像URLリストを取得する

    Returns
    -------
    user_doc : str
        ユーザーの傾向を反映した文章

    """
    user_item_obj = SearchData.objects.filter(userId=userId)[:user_num]

    user_img_list = [item.imageUrl for item in user_item_obj]

    return user_img_list


def _get_book_info_list(genre):
    """
    書籍情報リストを取得する

    Parameters
    ----------
    genre : str
        ジャンル名

    Returns
    -------
    item_list : list
        書籍情報リスト
    """

    # 楽天books api起動
    result_list = bookapi.get_book_data(genre)

    # 検索結果リストを生成
    item_list = []
    # リクエスト回数だけループ処理
    for result in result_list:
        # 書籍情報リスト取得
        items = result['Items']

        item_list += items

    return item_list
