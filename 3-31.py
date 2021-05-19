class Monster:
    def __init__(self, name, attack, defence):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.hp = 20
        print(f"{name}이 생성되었습니다.")

    def decrease_hp(self, hp):
        self.hp = self.hp - hp
        print(f"{self.name}의 체력이 {hp}만큼 감소하였습니다.")
        print(f"{self.name}의 남은 체력: {self.hp}")

    def show_info(self):
        print(f"몬스터 이름: {self.name}")
        print(f"공격력: {self.attack}")
        print(f"방어력: {self.defence}")
        print(f"체력: {self.hp}")

    def __del__(self):
        print(f"{self.name}객체가 삭제되었습니다.")


if __name__ == "__main__":
    화끈몬1 = Monster("화끈몬1", 4, 2)
    화끈몬2 = Monster("화끈몬2", 3, 3)
    화끈몬1.decrease_hp(2)
    화끈몬1.show_info()
    화끈몬2.show_info()
