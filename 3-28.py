import sys
import time


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)


if __name__ == "__main__":
    hello_msg = "몬스터 리그에 오신것을 환영합니다."
    delay_print(hello_msg)
