from rest_framework import serializers
from book_reco.domain.models import SearchData, RecommendData


class SearchModelSerializer(serializers.ModelSerializer):
    """
    検索結果Jsonのデータを定義する
    """

    # null許容
    itemCaption = serializers.CharField(max_length=300, allow_blank=True)

    class Meta:
        fields = (
            'id',
            'keyword',
            'genre',
            'title',
            'author',
            'itemCaption',
            'publisherName',
            'salesDate',
            'itemPrice',
            'itemUrl',
            'imageUrl',
        )
        model = SearchData


class RecommendModelSerializer(serializers.ModelSerializer):
    """
    レコメンド結果Jsonのデータを定義する
    """
    # null許容
    itemCaption = serializers.CharField(max_length=300, allow_blank=True)

    class Meta:
        fields = (
            # 'id',
            'genre',
            'title',
            'author',
            'itemCaption',
            'publisherName',
            'salesDate',
            'itemPrice',
            'itemUrl',
            'imageUrl',
        )
        model = RecommendData


class UserModelSerializer(serializers.ModelSerializer):
    """
    ユーザー情報

    """
