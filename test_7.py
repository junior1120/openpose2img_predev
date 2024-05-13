# moduleとmodel一覧を取得する
import requests

url = "http://127.0.0.1:7860"
# controlnet/module_listとcontrolnet/model_listをget
module_list = requests.get(url + "/controlnet/module_list").json()
model_list = requests.get(url + "/controlnet/model_list").json()
sdmodel_list = requests.get(url + "/sdapi/v1/sd-models").json()

# module_list["module_list"]の中にmoduleのリストが入っている
print(module_list["module_list"])
print(model_list["model_list"])  # model_list["model_list"]の中にmodelのリストが入っている
print(sdmodel_list)
