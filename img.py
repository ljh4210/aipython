from PIL import Image
import matplotlib.pyplot as plt

# 이미지 로딩
try:
    img_pillow = Image.open("image.jpg") # 이미지 파일 경로
    print(f"Pillow: 이미지 로드 성공 - 크기: {img_pillow.size}, 모드: {img_pillow.mode}")

    # 이미지 표시 (Matplotlib 사용)
    plt.imshow(img_pillow)
    plt.title("Pillow Loaded Image")
    plt.axis('off') # 축 숨기기
    plt.show()

    # 이미지 저장
    img_pillow.save("image_saved_pillow.png") # 다른 포맷으로 저장 가능

except FileNotFoundError:
    print("오류: image.jpg 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"Pillow 오류 발생: {e}")