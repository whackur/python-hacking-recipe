print("몬스터 리그에 오신것을 환영합니다.")
print("[1] 화끈몬\t[2] 축축몬\t[3] 수풀몬\n")
num = input(
    '플레이할 "몬스터"의 번호를 선택해 주세요: '
)  # 사용자의 숫자를 입력받습니다
name = input("당신의 이름을 입력해 주세요: ")  # 게임 플레이어의 이름을 입력합니다

print(num + "번을 선택하셨습니다. " + name + "님 환영합니다. ")
print("{}번을 선택하셨습니다. {}님 환영합니다.".format(num, name))
print("{0}번을 선택하셨습니다. {1}님 환영합니다.".format(num, name))
print("{1}번을 선택하셨습니다. {0}님 환영합니다.".format(num, name))
print("{num}번을 선택하셨습니다. {name}님 환영합니다.".format(num=100, name="마스터"))
print(f"{num}번을 선택하셨습니다. {name}님 환영합니다.")
