import time


def say_after(delay, what):
    time.sleep(delay)
    print(what)


def main():
    say_after(1, "hello")
    say_after(2, "world")


if __name__ == "__main__":
    print(f"started at {time.strftime('%X')}")
    main()
    print(f"finished at {time.strftime('%X')}")
