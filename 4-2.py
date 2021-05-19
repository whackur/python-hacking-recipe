from socket import *
import os
import struct


def parsing(host):
    # raw socket 생성 및 bind
    if os.name == "nt":
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP
    sock = socket(AF_INET, SOCK_RAW, sock_protocol)
    sock.bind((host, 0))

    # socket 옵션
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    # promiscuous mode 켜기
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_ON)

    packet_number = 0
    try:
        while True:
            packet_number += 1
            data = sock.recvfrom(65535)
            ip_headers, ip_payloads = parse_ip_header(data[0])
            print(f"{packet_number} th packet\n")
            print("version: ", ip_headers[0] >> 4)
            print("Header Length: ", ip_headers[0] & 0x0F)
            print("Type of Service: ", ip_headers[1])
            print("Total Length: ", ip_headers[2])
            print("Identification: ", ip_headers[3])
            print("IP Flags, Fragment Offset: ", flags_and_offset(ip_headers[4]))
            print("Time To Live: ", ip_headers[5])
            print("Protocol: ", ip_headers[6])
            print("Header Checksum:", ip_headers[7])
            print("Source Address: ", inet_ntoa(ip_headers[8]))
            print("Destination Address: ", inet_ntoa(ip_headers[9]))
            print("=" * 50)
    except KeyboardInterrupt:  # Ctrl-C key input
        if os.name == "nt":
            sock.ioctl(SIO_RCVALL, RCVALL_OFF)
            sock.close()


def parse_ip_header(ip_header):
    ip_headers = struct.unpack("!BBHHHBBH4s4s", ip_header[:20])
    ip_payloads = ip_header[20:]
    return ip_headers, ip_payloads


def flags_and_offset(int_num):
    byte_num = int_num.to_bytes(2, byteorder="big")
    x = bytearray(byte_num)
    flags_and_flagment_offset = bin(x[0])[2:].zfill(8) + bin(x[1])[2:].zfill(8)
    return (flags_and_flagment_offset[:3], flags_and_flagment_offset[3:])


if __name__ == "__main__":
    host = "192.168.0.5"  # 자신의 IP 주소로 변경
    print(f"Listening at [{host}]")
    parsing(host)
