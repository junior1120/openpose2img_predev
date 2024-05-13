# img2img
from PIL import Image
import webuiapi
api = webuiapi.WebUIApi()
PROMPT = """
masterpiece, best quality, 1girl, face, simple white background
""".strip()
NEGATIVE_PROMPT = """
easynegative
""".strip()
controlnet_units = []  # ControlNetオブジェクトのリスト用変数確保
controlnet_image0 = Image.open("test_2.png")  # ControlNetの入力に指定する画像をロード
controlnet_unit0 = webuiapi.ControlNetUnit(  # ControlNetUnitのインスタンス化
    input_image=controlnet_image0,  # ControlNetで参照する入力画像
    module="mediapipe_face",  # プリプロセッサ名
    model="control_v2p_sd15_mediapipe_face [9c7784a9]",  # Model名
    threshold_a=1,  # プリプロセッサの個別設定その1
    threshold_b=0.5,  # プリプロセッサの個別設定その2
)
controlnet_units.append(controlnet_unit0)  # リストに追加

result1 = api.txt2img(  # ControlNet_unit引数にリストを指定
    prompt=PROMPT, negative_prompt=NEGATIVE_PROMPT, controlnet_units=controlnet_units)
result1.image.save("test_6_1.png")

result2 = api.img2img(  # ControlNet_unit引数にリストを指定
    images=[result1.image], prompt="japanese girl", seed=5555, cfg_scale=6.5, denoising_strength=0.6)
result2.image.save("test_6_2.png")
