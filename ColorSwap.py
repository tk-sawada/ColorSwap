#!/usr/bin/env python3

import os
import cv2
import numpy as np
import tkinter
from tkinter import filedialog, ttk, Toplevel, Button, Label, messagebox, simpledialog

def close_window(window):
    window.destroy()

# GUIを非表示にします
root = tkinter.Tk()
root.withdraw()

# ユーザに処理の選択を尋ねる
option = simpledialog.askstring("Option", "Select an option:\n1. No Histogram Equalization\n2. Histogram Equalization\n3. Both", parent=root)

try:
    # 初期ディレクトリを設定します
    initial_directory = '/home/lunchbox/Pictures'

    # ユーザーにディレクトリを選択させます
    input_directory = filedialog.askdirectory(initialdir=initial_directory)
    print(f'Selected directory: {input_directory}')

    # 入力ディレクトリの名前を取得します
    input_directory_name = os.path.basename(input_directory)

    # 入力ディレクトリ内の全ての.jpgファイルをリストアップ
    jpg_files = [f for f in os.listdir(input_directory) if f.endswith('.JPG')]

    # 進捗バーのウィンドウを作成
    progress_window = Toplevel(root)
    progress_window.title("Processing Images")
    progress_label = ttk.Label(progress_window, text="Processing Images...")
    progress_label.grid(column=0, row=0)
    progress_bar = ttk.Progressbar(progress_window, length=200, mode='determinate', maximum=len(jpg_files))
    progress_bar.grid(column=0, row=1, pady=10)

    # 入力ディレクトリ内の全てのファイルを取得
    for i, filename in enumerate(jpg_files, start=1):
        # フルパスを取得
        filepath = os.path.join(input_directory, filename)

        # 画像を読み込む
        img = cv2.imread(filepath)

        # 画像をBGRからLABに変換
        img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

        # LAB色空間をチャネルごとに分割
        l_channel, a_channel, b_channel = cv2.split(img_lab)

        # AとBのチャネルを反転
        a_channel_inv = cv2.bitwise_not(a_channel)
        b_channel_inv = cv2.bitwise_not(b_channel)

        # 反転したチャネルと元のLチャネルを合成
        img_lab_inv = cv2.merge([l_channel, a_channel_inv, b_channel_inv])
        
        # LABからBGRに戻す
        img_bgr_inv = cv2.cvtColor(img_lab_inv, cv2.COLOR_Lab2BGR)
        
        # 処理結果を保存するディレクトリを指定（新規に作成します）
        if option == "1" or option == "3":
            output_directory_name = input_directory_name + '_LabSwapped'
            output_directory = os.path.join(os.path.dirname(input_directory), output_directory_name)
            os.makedirs(output_directory, exist_ok=True)
            output_filepath = os.path.join(output_directory, filename)
            cv2.imwrite(output_filepath, img_bgr_inv)
            print(f'Processed {filepath}, saved result as {output_filepath}')

        if option == "2" or option == "3":
            output_directory_name = input_directory_name + '_ColorSwapped'
            output_directory = os.path.join(os.path.dirname(input_directory), output_directory_name)
            os.makedirs(output_directory, exist_ok=True)
            # 画像をBGRからRGBに変換
            img_rgb_inv = cv2.cvtColor(img_bgr_inv, cv2.COLOR_BGR2RGB)

            # RGB色空間をチャネルごとに分割
            r_channel, g_channel, b_channel = cv2.split(img_rgb_inv)

            # RGB各色のチャネルに対してヒストグラム均等化を適用
            r_eq = cv2.equalizeHist(r_channel)
            g_eq = cv2.equalizeHist(g_channel)
            b_eq = cv2.equalizeHist(b_channel)

            # 均等化したチャネルを結合
            img_rgb_eq = cv2.merge([r_eq, g_eq, b_eq])

            # RGBからBGRに変換
            img_bgr_eq = cv2.cvtColor(img_rgb_eq, cv2.COLOR_RGB2BGR)

            # 結果を保存するファイルパスを指定
            output_filepath = os.path.join(output_directory, filename)

            # 結果を保存
            cv2.imwrite(output_filepath, img_bgr_eq)

            print(f'Processed {filepath}, saved result as {output_filepath}')

        # 進捗バーを更新
        progress_bar['value'] = i
        progress_label['text'] = f"Processing image {i} of {len(jpg_files)}..."
        progress_window.update_idletasks()

    # 終了メッセージを表示
    end_message_window = Toplevel(root)
    end_message_window.title("Finished")
    Label(end_message_window, text="Processing Completed Successfully.").grid(column=0, row=0)
    Button(end_message_window, text="OK", command=lambda: close_window(end_message_window)).grid(column=0, row=1, pady=10)

    # mainloopを開始
    root.mainloop()

except Exception as e:
    # エラーメッセージを表示
    error_message_window = Toplevel(root)
    error_message_window.title("Error")
    Label(error_message_window, text=f"An error occurred: {str(e)}").grid(column=0, row=0)
    Button(error_message_window, text="OK", command=lambda: close_window(error_message_window)).grid(column=0, row=1, pady=10)

    # mainloopを開始
    root.mainloop()
