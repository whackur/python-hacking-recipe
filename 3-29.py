from utils.display_test import delay_print

print(f"3-29.py의 __name__ : {__name__}")
if __name__ == "__main__":
    print(__name__)
    hello_msg = "몬스터 리그에 오신것을 환영합니다."
    delay_print(hello_msg)
