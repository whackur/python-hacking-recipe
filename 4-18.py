import socket
from time import time
import asyncio
from functools import partial

# ports = range(22,3000)
ports = [22, 80, 443, 445, 8080]
scan_target = "hakhub.net"


async def async_func():
    futures = [asyncio.ensure_future(port_scan(port)) for port in ports]
    results = await asyncio.gather(*futures)
    for result in results:
        if result["Open"]:
            print(result)


async def port_scan(port):
    tcp_request = partial(try_connect, port)
    resp = await loop.run_in_executor(None, tcp_request)
    return {"Port": port, "Open": resp[1], "Banner": resp[2]}


def try_connect(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        sock.connect((scan_target, port))
        sock.send("hello".encode())
        data = sock.recv(100).decode("utf-8", "replace")
        sock.close()
        return (port, True, data)

    except Exception as e:
        return (port, False, "")
    finally:
        sock.close()


if __name__ == "__main__":
    begin = time()
    print(f"Target Address: {scan_target}")
    print(f"Target Ports: {ports}")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_func())
    loop.close()
    end = time()
    print(f"실행 시간: {end - begin}")
