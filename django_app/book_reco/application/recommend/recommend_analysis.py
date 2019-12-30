"""
レコメンド書籍リストを生成するライブラリ
"""
import numpy as np
import requests
import traceback

from keras.applications.vgg16 import VGG16, preprocess_input
from PIL import Image
from io import BytesIO

recommend_num = 4  # おすすめ件数


def create_recommend_list(book_info_list, user_trend):
    """
    ユーザーの傾向に似た書籍リストを生成する

    Parameters
    ----------
    item_list : str
        検索ワード

    genre : str
        ジャンル名

    Returns
    -------
    sim_dict : dict
        ユーザーの傾向に近い書籍リスト

    """

    # 学習済みモデルクラスを生成
    conv_model = FeatuerModel()

    # ユーザー傾向の特徴量を算出
    # user_data = _get_img_from_url(user_trend)
    # user_feature = conv_model.featuer_extraction(user_data)
    user_feature = _get_user_feature(user_trend, conv_model)

    sim_dict = {}   # 類似度判定用辞書:item {isbn: similarity}
    ii = 0
    for book_info in book_info_list:
        ii = ii + 1
        print("dataset index" + str(ii))

        # 画像データのisbnと特徴量を獲得
        item_sbin = book_info["isbn"]
        item_float = [float(s) for s in book_info["feature"].split(" ")]
        item_feature = np.array(item_float)

        # ユーザー・書籍の特徴量から類似度を算出
        similarity = _cos_similarity(user_feature, item_feature)

        # 類似度判定
        if len(sim_dict) < recommend_num:
            # おすすめ書籍が設定値未満の場合、そのまま格納する
            sim_dict[item_sbin] = similarity
        elif min(sim_dict.values()) < similarity:
            # 類似度が最小のItemを削除する
            min_k = min(sim_dict, key=sim_dict.get)
            sim_dict.pop(min_k)
            sim_dict[item_sbin] = similarity

    return sim_dict


def _get_user_feature(user_img_list, conv_model):
    """
    ユーザー特徴量の平均値を算出する

    Parameters
    ----------
    user_img_list : str
        ユーザーの検索した画像URLリスト

    conv_model : VGG16モデル
       VGG16モデルラッパークラス

    Returns
    -------
    feature_ave : np.array
        ユーザー特徴量の平均値

    """

    user_feature_list = []

    for user_item in user_img_list:
        user_data = _get_img_from_url(user_item)
        user_feature = conv_model.featuer_extraction(user_data)
        user_feature_list.append(user_feature)

    feature_ave = sum(user_feature_list) / len(user_feature_list)
    return feature_ave


def _get_img_from_url(img_url):
    """
    画像URLから配列データを取得する

    Paramerters
    ------------
    img_url :str
        画像URL

    Returns
    ------------
    img_data : numpy.array
        画像データ配列
        配列の形状（244,244,3）

    """
    try:
        # URLから直接画像を読み込む
        response = requests.get(img_url)
        image = Image.open(BytesIO(response.content))
        img_data = np.array(image.resize((224, 224)))
    except Exception as e:
        traceback.print_exc(e)

    return img_data


def _cos_similarity(v1, v2):
    """
    二つのnumpy配列の類似度を求める
    """
    sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return sim


class FeatuerModel():

    """
    VGG16モデルラッパークラス

    Attributes
    ----------
    conv_base : VGG16()
       学習済みモデル（VGG16）

    """

    def __init__(self):
        """
        コンストラクタ
        学習済みモデルをロードする
        """
        self.conv_base = VGG16(include_top=False,
                               weights="imagenet",
                               input_shape=(224, 224, 3))

    def featuer_extraction(self, img_data):
        """
        画像データから特徴量を抽出する

        paramerters
        ------------
        model : VGG16
            VGG16モデル

        img_data : np.array
            画像データ配列
            配列の形状（244,244,3）

        results
        ------------
        img_feature :
            特徴量
        """

        x = np.expand_dims(img_data, axis=0)
        x = preprocess_input(x)

        features = self.conv_base.predict(x)
        features = features.flatten()
        return features
