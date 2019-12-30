"""
検索のメインロジックを担当
"""
from book_reco.domain.models import SearchData
from book_reco.application.api import book_api as bookapi


def search_book_info(userId, keyword, genre):
    """
    書籍データを取得する

    Parameters
    ----------
    user_id : str
        ユーザーID

    keyword : str
        検索ワード

    genre : str
        ジャンル名

    Returns
    -------
    obj : model.object
        検索結果

    """
    try:
        # 楽天books api起動
        response = bookapi.search_book_info(keyword, genre)
        # 書籍情報リスト取得
        items = response['Items']

        for item in items:

            # modelsを通してDBへの書き込みを行う
            SearchData.objects.create(
                keyword=keyword,
                genre=genre,
                userId=userId,
                title=item['Item']['title'],
                author=item['Item']['author'],
                itemCaption=item['Item']['itemCaption'],
                publisherName=item['Item']['publisherName'],
                salesDate=item['Item']['salesDate'],
                itemPrice=str(item['Item']['itemPrice']),
                itemUrl=item['Item']['itemUrl'],
                imageUrl=item['Item']['largeImageUrl']
            )

        # DBから最新の情報を1件取得
        obj = SearchData.objects.values().order_by(
            'id').reverse()[:len(items)]
        return obj

    except Exception as e:
        print('表示エラー')
        print(e)


if __name__ == 'main':
    search_book_info()

    None
