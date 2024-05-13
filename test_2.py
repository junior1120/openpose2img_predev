# シンプルな画像生成テスト
import webuiapi

api = webuiapi.WebUIApi()  # WebUIAPIのインスタンスを作成
PROMPT = "masterpiece, best quality, 1girl, standing, crossed arms"
result1 = api.txt2img(prompt=PROMPT)  # APIを呼び出している
result1.image.save("test_2.png")  # 生成画像を保存する
