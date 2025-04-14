#아스키 코드 그림 출력하기

#만약에 1을 입력하면 1번 캐릭터 출력
#만약에 2를 입력하면 2번 캐릭터 출력
#3을 입력하면 3번 캐릭터 출력
# 아니면(잘못입력하면) 잘못 입력했다고 출력

def print_mygame():
    print("그림 출력 프로그램")
    print("======================")
    print("1.강아지")
    print("2.고양이")
    print("3.햄스터")
    print("0.종료")
    print("======================")
    n = int(input("선택: "))

    if n == 0:
        return False  # 종료 신호
    elif n == 1:
        print(r"""
     / \__
    (    @\___
    /         O
   /   (_____/
  /_____/ U
        """)
    elif n == 2:
        print(r"""
     /\_/\  
    ( o.o ) 
     > ^ <
        """)
    elif n == 3:
        print(r"""
 (\_/)
 (•ㅅ•)
 / 　 づ
        """)
    else:
        print("1, 2, 3 또는 0을 입력해주세요.")

    print()  # 줄바꿈
    return True

# 무한반복 실행, 0 입력 시 종료
print("0 입력하면 종료되는 프로그램 시작")
while True:
    if not print_mygame():
        break
print("0 입력하면 종료되는 프로그램 종료")