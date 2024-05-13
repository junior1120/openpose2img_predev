# 　ネガティブプロンプトの追加
from pprint import pprint
import webuiapi
api = webuiapi.WebUIApi()
PROMPT = """
masterpiece, best quality, 1girl, face, simple white background
""".strip()
NEGATIVE_PROMPT = """
easynegative
""".strip()
result1 = api.txt2img(prompt=PROMPT, negative_prompt=NEGATIVE_PROMPT)
result1.image.save("test_3.png")
pprint(result1.info)
