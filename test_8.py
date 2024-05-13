# SDXL版Openposeを使用する
import time
from PIL import Image
import webuiapi
start = time.perf_counter()  # 計測開始
api = webuiapi.WebUIApi()
api.default_steps = 1
options = {}
options['sd_model_checkpoint'] = 'sd_xl_turbo_1.0.safetensorsmaste [2e58e3704b]'
api.set_options(options)
PROMPT = """
masterpiece, best quality, 1girl, simple white background, 16k, best quality
""".strip()
NEGATIVE_PROMPT = """
easynegative
""".strip()
controlnet_units = []  # ControlNetオブジェクトのリスト用変数確保
controlnet_image0 = Image.open("test_2.png")  # ControlNetの入力に指定する画像をロード
controlnet_unit0 = webuiapi.ControlNetUnit(  # ControlNetUnitのインスタンス化
    input_image=controlnet_image0,  # ControlNetで参照する入力画像
    module="openpose",  # プリプロセッサ名
    model="t2i-adapter_xl_openpose [18cb12c1]"  # Model名
)
controlnet_units.append(controlnet_unit0)  # リストに追加
result1 = api.txt2img(  # ControlNet_unit引数にリストを指定
    prompt=PROMPT, negative_prompt=NEGATIVE_PROMPT, controlnet_units=controlnet_units,
    cfg_scale=1, width=512, height=512)
result1.image.save("test_8_1.png")
result1.images[1].save("test_8_2.png")
print(result1.image)
end = time.perf_counter()  # 計測終了
print('{:.2f}'.format((end-start)/60))  # 87.97(秒→分に直し、小数点以下の桁数を指定して出力)
