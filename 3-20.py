화끈몬_체력 = 100
print(f"화끈몬의 체력: {화끈몬_체력}")
while 화끈몬_체력 > 0:
    데미지 = None
    while True:
        데미지 = int(input("가할 데미지 (데미지가 0이면 턴을 넘김): "))
        if 데미지 < 0:
            print("가할 데미지는 최소 0입니다.")
            continue
        elif 데미지 == 0:
            print("턴을 넘깁니다.")
        elif 데미지 <= 20:
            print("효과는 미미했다.")
            break
        elif 데미지 <= 30:
            print("효과는 굉장했다.")
            break
        else:
            print("효과는 치명적이었다.")
            break
    화끈몬_체력 = 화끈몬_체력 - 데미지
    if 화끈몬_체력 < 0:
        화끈몬_체력 = 0
    print(f"화끈몬이 공격받아 체력 {화끈몬_체력} 이 남았습니다.")
    if 화끈몬_체력 <= 0:
        print(f"화끈몬이 쓰러졌습니다.")
