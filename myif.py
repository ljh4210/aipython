#아스키 코드 그림 출력하기

print("그림 출력 프로그램")
print("======================")
print("1.강아지")
print("2.고양이")
print("3.햄스터")
print("======================")
number = int(input("선택: "))


#만약에 1을 입력하면 1번 캐릭터 출력
#만약에 2를 입력하면 2번 캐릭터 출력
#3을 입력하면 3번 캐릭터 출력
# 아니면(잘못입력하면) 잘못 입력했다고 출력


# 입력된 숫자에 따라 캐릭터 출력
if number == 1:
    print("강아지")
    
elif number == 2:
    print("고양이")
    
elif number == 3:
    print("햄스터")
    
else:
    print("잘못된 숫자입니다. 1에서 3 사이의 숫자를 입력하세요.")


puppy = '''
  / \__/ \
 (  ◕ ᴥ ◕ )
  \______/
'''

kitty = '''
 /\_/\ 
( o.o )
 > ^ < 
'''

hamster = '''
  ,_   . .
 ( v ^   .)
  \ '---' /
'''

# 사용자에게 입력을 받습니다.
choice = input('1번을 입력하면 강아지, 2번을 입력하면 고양이, 3번을 입력하면 햄스터를 출력합니다: ')

# 입력에 따라 아스키 아트를 출력합니다.
if choice == '1':
    print(puppy)
elif choice == '2':
    print(kitty)
elif choice == '3':
    print(hamster)
else:
    print('잘못된 선택입니다.')