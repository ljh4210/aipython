def print_multiplication_table(number):
    print(f"== {number}단 ==")
    for i in range(1, 10):
        print(f"{number} x {i} = {number * i}")

# 사용자로부터 숫자 입력받기
try:
    num = int(input("구구단을 출력할 숫자를 입력하세요: "))
    print_multiplication_table(num)
except ValueError:
    print("올바른 숫자를 입력해주세요.")
