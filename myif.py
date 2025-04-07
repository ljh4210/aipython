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
    print("======================")
    n = int(input("선택:"))

    if n == 1:
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
        print("1, 2, 3 중에서 선택해주세요.")
    print()  
# 입력된 숫자에 따라 캐릭터 출력

for i in range(5):
    print_mygame()


#무한반복,0종료료
while True:
    print_mygame()