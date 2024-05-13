# txt2img openposeを出力させる
from PIL import Image
import webuiapi
api = webuiapi.WebUIApi()
options = {}
options['sd_model_checkpoint'] = 'v1.5.ckpt [cc6cb27103]'
api.set_options(options)
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
    module="openpose",  # プリプロセッサ名
    model="control_v11p_sd15_openpose_fp16 [73c2b67d]"  # Model名
)
controlnet_units.append(controlnet_unit0)  # リストに追加
result1 = api.txt2img(  # ControlNet_unit引数にリストを指定
    prompt=PROMPT, negative_prompt=NEGATIVE_PROMPT, controlnet_units=controlnet_units)
result1.image.save("test_5_1.png")
result1.images[1].save("test_5_2.png")
print(result1.image)
