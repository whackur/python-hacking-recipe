def select_monster():
    print("몬스터 리그에 오신것을 환영합니다.")
    monsters = ["화끈몬", "축축몬", "수풀몬"]
    for index, monster in enumerate(monsters):
        print(f"[{index + 1}] {monster}\t", end="")
    # 사용자의 숫자를 입력받습니다
    selected_num = input('\n플레이할 "몬스터"의 번호를 선택해 주세요.: ')
    # 게임 플레이어의 이름을 입력합니다
    user_name = input("당신의 이름을 입력해 주세요.: ")
    # 사용자가 선택한 몬스터
    user_monster = monsters[int(selected_num) - 1]
    print(f"[{selected_num}] {user_monster}을 선택하셨습니다.")
    print(f"{user_name}님 환영합니다.")


if __name__ == "__main__":
    select_monster()
