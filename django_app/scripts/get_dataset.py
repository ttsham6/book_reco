"""
データセット作成Module
"""
import numpy as np
import requests
import csv
from book_reco.application.api import book_api
from book_reco.domain.models import DatasetData
from PIL import Image
from io import BytesIO
from keras.applications.vgg16 import VGG16, preprocess_input


def run():
    """
    テストコード：特徴量データセット作成用
    書籍ID（ISBNコード、特徴量ベクトル）をCSVファイルに出力する
    """

    # 書籍データを取得
    book_info_list = book_api.create_imagedataset()

    # 書籍データをDBに保存

    # VGG16モデルクラスを設定
    conv_model = FeatuerModel()

    with open('feature_dataset.csv', 'w', newline="") as f:
        writer = csv.writer(f)

        for book_info in book_info_list:
            try:

                # ISBN取得
                isbn = book_info["isbn"]

                if not isbn.startswith('978'):
                    continue

                # 書籍データをDBに保存
                DatasetData.objects.create(
                    isbn=isbn,
                    title=book_info['title'],
                    author=book_info['author'],
                    itemCaption=book_info['itemCaption'],
                    publisherName=book_info['publisherName'],
                    salesDate=book_info['salesDate'],
                    itemPrice=str(book_info['itemPrice']),
                    itemUrl=book_info['itemUrl'],
                    imageUrl=book_info['largeImageUrl']
                )

                # 書籍データからURLを取得
                img_url = book_info["largeImageUrl"]

                # URLから直接画像を読み込む
                response = requests.get(img_url)
                image = Image.open(BytesIO(response.content))
                image_data = np.array(image.resize((224, 224)))

            except Exception as e:
                print("response")
                print(e)
                # print("")
                continue

            # 特徴量を算出
            try:
                feature = conv_model.featuer_extraction(image_data)
            except Exception as e:
                print("feature")
                print(e)
                continue

            feature = ' '.join(map(str, feature))

            print("index: " + str(book_info_list.index(book_info)))
            print("isbn: " + str(isbn))

            # csvファイルに出力
            row = [isbn, feature]
            writer.writerow(row)

        f.close()

    print("Result")
    # result_df.to_csv(os.path.join(
    #     IMG_FILE_DIR, "feature_dataset.csv"), encoding='utf-8-sig')


class FeatuerModel():

    def __init__(self):

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


if __name__ == '__main__':
    # 動作確認

    # _test_1()
    # create_dataset()

    # _input_dataset()

    None
