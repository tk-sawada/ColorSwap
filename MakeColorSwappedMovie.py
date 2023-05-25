import os
import cv2
import numpy as np
import tkinter
from tkinter import filedialog, ttk, Toplevel, Button, Label, messagebox, simpledialog
from moviepy.editor import VideoFileClip, AudioFileClip

def process_frame(img):
    # 画像処理のコード（省略）

root = tkinter.Tk()
root.withdraw()

try:
    input_file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4"), ("M2TS files", "*.m2ts"), ("MTS files", "*.MTS")])
    clip = VideoFileClip(input_file_path)
    audio = clip.audio

    # オリジナルの動画の音声の長さを取得
    audio_duration = audio.duration

    processed_clip = clip.fl_image(process_frame)
    # 映像のフレームレートを調整して音声の長さに合わせる
    new_fps = processed_clip.duration / audio_duration

    temp_output_file_path = os.path.splitext(input_file_path)[0] + "_processed_temp.mp4"
    output_file_path = os.path.splitext(input_file_path)[0] + "_processed.mp4"

    # ビデオクリップのみを一旦保存します
    processed_clip.write_videofile(temp_output_file_path, fps=new_fps)  # Apply the new fps here

    # ビデオクリップを再度読み込み、音声を付加します
    final_clip = VideoFileClip(temp_output_file_path)
    final_clip = final_clip.set_audio(audio)
    final_clip.write_videofile(output_file_path)

    # 一時ファイルを削除します
    os.remove(temp_output_file_path)

    messagebox.showinfo("Success", f"Processing completed. Output saved as {output_file_path}")

except Exception as e:
    messagebox.showerror("Error", str(e))

root.destroy()  # Close the Tkinter window and exit the program
