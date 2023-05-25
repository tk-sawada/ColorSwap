import os
import cv2
import numpy as np
import tkinter
import subprocess
from tkinter import filedialog, ttk, Toplevel, Button, Label, messagebox, simpledialog
from moviepy.editor import VideoFileClip, AudioFileClip

def process_frame(img):
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

    return img_rgb_eq


def convert_to_cfr(input_file_path, output_file_path, fps):
    command = ['ffmpeg', '-i', input_file_path, '-vsync', 'cfr', '-r', str(fps), output_file_path]
    subprocess.run(command, check=True)

def main():
    root = tkinter.Tk()
    root.withdraw()

    try:
        input_file_path = filedialog.askopenfilename(filetypes=[ ("MTS files", "*.MTS"), ("M2TS files", "*.m2ts"), ("MP4 files", "*.mp4")])

        cfr_file_path = os.path.splitext(input_file_path)[0] + "_cfr.mp4"
        clip = VideoFileClip(input_file_path)
        convert_to_cfr(input_file_path, cfr_file_path, clip.fps)

        clip_cfr = VideoFileClip(cfr_file_path)
        audio = clip_cfr.audio

        processed_clip = clip_cfr.fl_image(process_frame)

        temp_output_file_path = os.path.splitext(input_file_path)[0] + "_processed_temp.mp4"
        output_file_path = os.path.splitext(input_file_path)[0] + "_processed.mp4"

        processed_clip.write_videofile(temp_output_file_path, fps=clip_cfr.fps) 

        final_clip = VideoFileClip(temp_output_file_path)
        final_clip = final_clip.set_audio(audio)
        final_clip.write_videofile(output_file_path)

        os.remove(temp_output_file_path)
        os.remove(cfr_file_path)

        messagebox.showinfo("Success", f"Processing completed. Output saved as {output_file_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

    root.destroy()  # Close the Tkinter window and exit the program

if __name__ == "__main__":
    main()
