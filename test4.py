#함수만들기
def hello():
    print("hello world")

#함수호출 (실행)
hello()


def hello_name(name):
    print(f"안녕 {name}야")

name = input("이름을 입력하시오:")
hello_name(name)

#연산하는함수
def cal(n1, n2, op): #1, 2, + 
    r = 0
    if op == "+":
        r = n1 + n2

    elif op == "-":
        r = n1 - n2
    else:
        print("잘못입력")
    return r

r = cal(2, 1, "+")
print(f"두 수를 더한 값{r}")
r = cal(2, 1, "-")
print(f"두 수를 뺀 값{r}")