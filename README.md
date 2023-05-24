# ColorSwap
赤外線写真(.JPG)、赤外線動画(.mp4,.m2ts)をカラースワップ(LABカラースワップ)を行うプログラムです。
 
## 簡単な説明

## MakeColorSwappedPicture.py

赤外線写真を撮ったときにカラースワップ(LAB～スワップ)を1枚ずつ行うのが面倒だったためプログラムを作成して自動化(MakeColorSwappedPicture.py)しました。

フォルダ選択の画面で赤外線写真が入ったフォルダを選択すると、「フォルダ名_LabSwapped」または「フォルダ名_ColorSwapped」、もしくは両方が作成されフォルダ内にカラースワップされた写真が保存されます。

色が飛んでしまった写真はレタッチしても綺麗な仕上がりにすることが難しいので、LABカラースワップ+ヒストグラム均等化を行った画像で色映りを確認したうえで、LABスワップを行った画像をGIIMPなりPhotoshopなりで加工するとよいと思います。
 
## MakeColorSwappedMovie.py

mp4またはm2tsの動画ファイルをLABカラースワップ+ヒストグラム均等化を行い、カラースワップした動画を作成します。

MakeColorSwappedPicture.pyでは写真のフォルダを選択しますが、MakeColorSwappedMovie.pyでは動画ファイルを選択します。

## 機能

### MakeColorSwappedPicture.py
- 機能1（LABカラースワップを行った画像を保存）
- 機能2（LABカラースワップ+ヒストグラム均等化を行った画像を保存）
- 機能3（機能1、機能2の両方を行う）
 
### MakeColorSwappedMovie.py
- 機能1（LABカラースワップ+ヒストグラム均等化を行った動画を保存）

## 必要要件

このスクリプトを実行するためには、Python3が必要であり、以下のパッケージが必要です。

- OpenCV (cv2)
- NumPy
- tkinter
- moviepy

### Linux（Ubuntu）

Pythonのインストール:
```
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
```
必要なPythonパッケージのインストール：
```
pip3 install opencv-python
pip3 install numpy
pip3 install moviepy
```
tkinterはPython3がインストールされている場合、既にインストールされていますが、インストールされていない場合は以下のコマンドでインストールできます:
```
sudo apt-get install python3-tk
```
### Windows

Windowsでは、Pythonを公式ウェブサイトからダウンロードしてインストールします。インストール時に、"Add Python to PATH"のオプションを選択してください。

次に、コマンドプロンプトを開き、以下のコマンドを実行して必要なパッケージをインストールします：
```
pip install opencv-python
pip install numpy
pip install moviepy
```
tkinterはPythonがインストールされている場合、既にインストールされています。

### Mac OS

まず、Homebrewを使用してPythonをインストールします。Homebrewがまだインストールされていない場合は、ターミナルを開き、以下のコマンドを実行します：
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
次に、Homebrewを使用してPython3をインストールします：

```
brew install python3
```

ここで、pip3が自動的にインストールされるはずです。

そして、以下のコマンドを使って必要なPythonパッケージをインストールします：
```
pip3 install opencv-python
pip3 install numpy
pip3 install moviepy
```

tkinterはPython3がインストールされている場合、既にインストールされています。


## 使い方

### MakeColorSwappedPicture.py

1. python3 MakeColorSwappedPicture.py
2. 画面に従い、1,2,3のいずれかを選択
3. 画像が出力されます
 
### MakeColorSwappedMovie.py

1. python3 MakeColorSwappedMovie.py
2. 動画が出力されます

## インストールとテスト
 
```
git clone https://github.com/tk-sawada/ColorSwap
cd ColorSwap
sudo chmod +x ./MakeColorSwappedPicture.py ./MakeColorSwappedMovie.py
python3 ./ColorSwap.py
```
 
## その他
 
一部ChatGPTにプログラムを書いてもらいました。
 
## 作者
[@tkyswd](https://www.instagram.com/tkyswd/)

## ライセンス
 
[MIT](http://TomoakiTANAKA.mit-license.org)</blockquote>
