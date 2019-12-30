from django.db import models

# Create your models here.


class SearchData(models.Model):
    """
    検索結果モデル

    Attributes
    ----------
    userId : str
        ユーザーID
    keyword : str
        検索ワード
    genre : str
        ジャンル
    title : str
        書籍タイトル
    author : str
        著者
    itemCaption : str
        アイテム説明
    publsherName : str
        出版社
    size : str
        書籍サイズ
        1:単行本
        2:文庫
        3:新書
        4:全集・双書
        5:事・辞典
        6:図鑑
        7:絵本
        8:カセット,CDなど
        9:コミック
        10:ムックその他
    salesDate : str
        発売日
    itemProce : str
        価格
    itemUrl : str
        書籍情報URL
    imageUrl : str
        画像URL

    """
    userId = models.CharField(max_length=20, default='')
    keyword = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    itemCaption = models.CharField(max_length=500)
    publisherName = models.CharField(max_length=30)
    salesDate = models.CharField(max_length=20)
    itemPrice = models.CharField(max_length=20)
    itemUrl = models.CharField(max_length=300)
    imageUrl = models.CharField(max_length=300)


class RecommendData(models.Model):
    """
    おすすめ情報モデル

    Attributes
    ----------
    userId : str
        ユーザーID
    genre : str
        ジャンル
    title : str
        書籍タイトル
    author : str
        著者
    itemCaption : str
        アイテム説明
    publsherName : str
        出版社
    size : str
        書籍サイズ
        1:単行本
        2:文庫
        3:新書
        4:全集・双書
        5:事・辞典
        6:図鑑
        7:絵本
        8:カセット,CDなど
        9:コミック
        10:ムックその他
    salesDate : str
        発売日
    itemProce : str
        価格
    itemUrl : str
        URL

    """
    userId = models.CharField(max_length=20, default='')
    genre = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    itemCaption = models.CharField(max_length=500)
    publisherName = models.CharField(max_length=30)
    salesDate = models.CharField(max_length=20)
    itemPrice = models.CharField(max_length=20)
    itemUrl = models.CharField(max_length=300)
    imageUrl = models.CharField(max_length=300)


class DatasetData(models.Model):
    """
    データセットモデル
    （おすすめ情報提供用）

    Attributes
    ----------
    title : str
        書籍タイトル
    author : str
        著者
    itemCaption : str
        アイテム説明
    publsherName : str
        出版社
    size : str
        書籍サイズ
        1:単行本
        2:文庫
        3:新書
        4:全集・双書
        5:事・辞典
        6:図鑑
        7:絵本
        8:カセット,CDなど
        9:コミック
        10:ムックその他
    salesDate : str
        発売日
    itemProce : str
        価格
    itemUrl : str
        URL

    """
    isbn = models.CharField(max_length=30, default='')
    title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=30, default='')
    itemCaption = models.CharField(max_length=500, default='')
    publisherName = models.CharField(max_length=30, default='')
    salesDate = models.CharField(max_length=20, default='')
    itemPrice = models.CharField(max_length=20, default='')
    itemUrl = models.CharField(max_length=300, default='')
    imageUrl = models.CharField(max_length=300, default='')


class UserData(models.Model):
    """
    ユーザー情報

    Attributes
    ----------
    userId : str
        ユーザーID
    password : str
        パスワード

    """
    userId = models.CharField(primary_key=True, max_length=20, default='')
    password = models.CharField(max_length=20, default='')
