from rich import print

# 색상과 스타일이 적용된 출력
# print("[bold red]안녕하세요[/bold red] 파이썬 세계!")

# 데이터 구조 출력
# data = {"이름": "홍길동", "나이": 30, "취미": ["독서", "영화감상", "코딩"]}
# print(data)

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.progress import Progress
from rich.prompt import IntPrompt
from rich.theme import Theme
from rich.live import Live
from rich.align import Align
import time
import random

# 사용자 정의 테마 생성
custom_theme = Theme({
    "title": "bold cyan",
    "menu_item": "yellow",
    "selected": "bold green",
    "error": "bold red",
    "exit": "dim italic",
    "animal": "bold magenta",
    "loading": "bold blue",
    "success": "green",
})

console = Console(theme=custom_theme)

def show_loading(message="로딩 중..."):
    """로딩 애니메이션을 표시합니다"""
    with console.status(f"[loading]{message}[/loading]", spinner="dots"):
        # 랜덤한 시간(0.5~1.5초) 동안 로딩 애니메이션 표시
        time.sleep(random.uniform(0.5, 1.5))

def create_menu():
    """메뉴 테이블을 생성합니다"""
    table = Table(show_header=False, box=None, expand=True)
    table.add_column("Menu")
    
    title = Text("🐾 귀여운 동물 출력 프로그램 🐾", style="title")
    header = Align.center(title)
    
    menu_items = [
        Text("1. 강아지 🐶", style="menu_item"),
        Text("2. 고양이 🐱", style="menu_item"),
        Text("3. 햄스터 🐹", style="menu_item"),
        Text("0. 종료 👋", style="exit")
    ]
    
    table.add_row(header)
    table.add_row("=" * 50)
    
    for item in menu_items:
        table.add_row(item)
        
    table.add_row("=" * 50)
    
    return Panel(table, border_style="cyan")

def animate_dog():
    """강아지 애니메이션 프레임들"""
    frames = [
        r"""
     / \__
    (    @\___
    /         O
   /   (_____/
  /_____/ U  
        """,
        r"""
     / \__
    (    @\___
    /         O
   /   (_____/
  /_____/  U 
        """,
        r"""
     / \__
    (    @\___
    /         O
   /   (_____/
  /_____/U   
        """,
        r"""
     / \__
    (    @\___
    /        O
   /   (____O/
  /_____/ U  
        """
    ]
    return frames

def animate_cat():
    """고양이 애니메이션 프레임들"""
    frames = [
        r"""
     /\_/\  
    ( o.o ) 
     > ^ <  
        """,
        r"""
     /\_/\  
    ( -.o ) 
     > ^ <  
        """,
        r"""
     /\_/\  
    ( o.- ) 
     > ^ <  
        """,
        r"""
     /\_/\  
    ( o.o ) 
     > - <  
        """
    ]
    return frames

def animate_hamster():
    """햄스터 애니메이션 프레임들"""
    frames = [
        r"""
 (\_/)
 (•ㅅ•)
 / 　 づ
        """,
        r"""
 (\_/)
 (•ㅅ-)
 / 　 づ
        """,
        r"""
 (\_/)
 (-ㅅ•)
 / 　 づ
        """,
        r"""
 (\_/)
 (•ㅅ•)
 /づ 　 
        """
    ]
    return frames

def animate_animal(animal_frames, animal_name, sound, duration=5):
    """동물 애니메이션을 표시합니다"""
    start_time = time.time()
    end_time = start_time + duration
    frame_count = len(animal_frames)
    
    with Live(refresh_per_second=10) as live:
        while time.time() < end_time:
            # 프레임 인덱스 계산 (시간에 따라 변화)
            frame_idx = int((time.time() - start_time) * 4) % frame_count
            current_frame = animal_frames[frame_idx]
            
            # 패널 생성
            animal_panel = Panel(
                Text(current_frame, style="animal"),
                title=f"{animal_name} 등장!", 
                subtitle=sound,
                border_style="magenta",
                width=30
            )
            
            # 애니메이션 프레임 업데이트
            live.update(animal_panel)
            time.sleep(0.1)

def print_mygame():
    # 메뉴 표시
    console.print(create_menu())
    
    # 사용자 입력
    try:
        n = IntPrompt.ask("선택", console=console)
    except ValueError:
        console.print("[error]숫자만 입력해주세요![/error]")
        return True
    
    if n == 0:
        # 종료 진행바 표시
        with Progress() as progress:
            task = progress.add_task("[cyan]종료 중...", total=100)
            while not progress.finished:
                progress.update(task, advance=random.uniform(0.5, 2.0))
                time.sleep(0.05)
        console.print("[exit]프로그램을 종료합니다. 안녕히 가세요![/exit]")
        return False  # 종료 신호
    
    elif n == 1:
        show_loading("강아지를 불러오는 중...")
        dog_frames = animate_dog()
        console.print("[success]멍멍! 반갑습니다![/success]")
        animate_animal(dog_frames, "강아지", "멍멍! 🐶")
        
    elif n == 2:
        show_loading("고양이를 불러오는 중...")
        cat_frames = animate_cat()
        console.print("[success]야옹~ 안녕하세요![/success]")
        animate_animal(cat_frames, "고양이", "야옹~ 🐱")
        
    elif n == 3:
        show_loading("햄스터를 불러오는 중...")
        hamster_frames = animate_hamster()
        console.print("[success]찍찍! 만나서 반가워요![/success]")
        animate_animal(hamster_frames, "햄스터", "찍찍! 🐹")
        
    else:
        console.print("[error]1, 2, 3 또는 0을 입력해주세요.[/error]")

    console.print()
    # 계속하려면 아무 키나 누르라는 메시지
    console.print("[dim]계속하려면 Enter 키를 누르세요...[/dim]")
    input()
    return True

# 프로그램 시작
def main():
    # 시작 화면 애니메이션
    welcome_text = Text("🎮 동물 친구들 프로그램을 시작합니다 🎮", style="bold cyan")
    welcome_panel = Panel(welcome_text, border_style="green")
    
    with Live(welcome_panel, refresh_per_second=4) as live:
        for i in range(5, 0, -1):
            welcome_text = Text(f"🎮 동물 친구들 프로그램을 시작합니다 🎮\n\n{i}초 후에 시작됩니다...", style="bold cyan")
            welcome_panel = Panel(welcome_text, border_style="green")
            live.update(welcome_panel)
            time.sleep(1)
    
    console.clear()
    
    # 메인 루프
    while True:
        console.clear()  # 화면 초기화
        if not print_mygame():
            break
    
    # 종료 메시지
    console.print(Panel(Text("프로그램이 종료되었습니다. 다음에 또 만나요!", style="bold cyan"), border_style="red"))

if __name__ == "__main__":
    main()