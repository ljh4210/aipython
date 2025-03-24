# num = int(input("구구단을 출력할 숫자를 입력하세요: "))
s_num = (input("구구단을 출력할 숫자를 입력하세요: "))
# print(f"{s_num}단:")
print(f"{s_num}단:")
# 넘버가 문자열이니까 숫자로 변경해줘야
num = int(s_num)
result = num * 2
print(result)