## StableDiffusion WebUIのAPIを介してOpenposeからリアルタイム画像生成を行います。(仮実装中です)

### 目的
* Openposeのフレーム情報を用いてリアルタイム画像生成を行う
 →リアルタイム性を担保するためにSDXL Turboを使用する

### 現状の課題
* 生成画像の質が低い
* Openposeの反映度合いが低い
 →Openposeのパラメータを改善する or Openposeのモデル変更

### 内容説明
* StableDiffusionPy:venvの環境設定ディレクトリ
* test_1.py:動作確認用コード
* test_2.py:単純な画像生成を行うコード
* test_3.py::上記にネガティブプロンプトの要素を追加したコード
* test_4.py:ControlNet(Mediapipe)を使用して画像生成するコード
* test_5.py:ControlNet(Openpose)+SD1.5を使用して画像生成するコード
* test_6.py:img2imgを行うためのサンプルコード(関係なし)
* test_7.py:WebUIにインストールしたModuleとModel、Stable DiffusionのModel一覧を出力するためのコード
* test_8.py:ControlNet(Openpose)+SDXL Turboを使用して画像生成するコード
