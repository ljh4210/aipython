import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(
        title="이미지 파일 선택",
        filetypes=(("이미지 파일", "*.png;*.jpg;*.jpeg;*.gif"), ("모든 파일", "*.*"))
    )
    if file_path:
        try:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.image = photo  # Keep a reference!
        except Exception as e:
            print(f"오류 발생: {e}")
            tk.messagebox.showerror("오류", f"이미지 파일을 열 수 없습니다: {e}")

# 메인 윈도우 생성
window = tk.Tk()
window.title("간단한 이미지 뷰어")

# 이미지 표시를 위한 Label 생성
image_label = tk.Label(window)
image_label.pack(padx=10, pady=10)

# "이미지 열기" 버튼 생성
open_button = tk.Button(window, text="이미지 열기", command=open_image)
open_button.pack(pady=5)

# 프로그램 실행
window.mainloop()