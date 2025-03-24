# 숫자 두 개 입력하면
# +, -, *, / 를 출력해주는 프로그램을 만들자
# 두 숫자 입력받기
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 사칙연산 수행
덧셈 = num1 + num2
뺄셈 = num1 - num2
곱셈 = num1 * num2

# 나눗셈 (0으로 나누는 경우 처리)
if num2 != 0:
    나눗셈 = num1 / num2
else:
    나눗셈 = "불가능 (0으로 나눌 수 없음)"

# 결과 출력
print(f"\n===== 계산 결과 =====")
print(f"{num1} + {num2} = {덧셈}")
print(f"{num1} - {num2} = {뺄셈}")
print(f"{num1} * {num2} = {곱셈}")
print(f"{num1} / {num2} = {나눗셈}")

    