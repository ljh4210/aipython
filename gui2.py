import tkinter as tk
from PIL import Image, ImageTk

def show_Dog():
    try:
        image = Image.open("Dog.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    except Exception as e:
        tk.messagebox.showerror("오류", f"강아지 이미지 파일을 열 수 없습니다: {e}")

def show_cat():
    try:
        image = Image.open("cat.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    except Exception as e:
        tk.messagebox.showerror("오류", f"고양이 이미지 파일을 열 수 없습니다: {e}")

def show_hamster():
    try:
        image = Image.open("hamster.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    except Exception as e:
        tk.messagebox.showerror("오류", f"햄스터 이미지 파일을 열 수 없습니다: {e}")

# 메인 윈도우 생성
window = tk.Tk()
window.title("동물 이미지 뷰어")

# 이미지 표시를 위한 Label 생성
image_label = tk.Label(window)
image_label.pack(padx=10, pady=10)

# 버튼 생성
dog_button = tk.Button(window, text="강아지", command=show_Dog)
dog_button.pack(pady=5)

cat_button = tk.Button(window, text="고양이", command=show_cat)
cat_button.pack(pady=5)

hamster_button = tk.Button(window, text="햄스터", command=show_hamster)
hamster_button.pack(pady=5)

# 프로그램 실행
window.mainloop()