from pythonping import ping
from time import time


def icmp_scan():
    ip_addresses = ["33.22.143.1", "8.8.8.8", "google.com"]
    for ip_address in ip_addresses:
        print(f"Ping Target => {ip_address}")
        ping(ip_address, timeout=1, count=1, verbose=True)


if __name__ == "__main__":
    begin = time()
    icmp_scan()
    end = time()
    print(f"실행 시간: {end - begin}")
