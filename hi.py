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