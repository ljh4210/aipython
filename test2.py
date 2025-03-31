v = int(input("입력값: "))
#만약 입력 받은 값이 0이면 0이다.
#if v == "0": 이건 문자열비교
#숫자인지 문자인지 알고싶으면? 밑에코드 치면 숫자는 int 문자는 str이라고 뜸
print(type(v))
print("문자로 변환")
v = str(v)
print(type(v))

if v == 0:
    print("0이다")

#만약 입력 받은 값이 0이 아니면 0이 아니다.

if v != 0:
    print("0이아니다")

 #만약 입력 받은 값이 0이면 0이다를 출력 아니면 0이 아니다 출력
 if v == 0:
    print("0이다")
else:
    print("0이아니다")