# utils/display_test.py
import sys
import time

print(f"display_test.py의 __name__ : {__name__}")


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
