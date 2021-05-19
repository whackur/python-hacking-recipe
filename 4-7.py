from socket import *
import os
import struct


def parse_ip_header(payload):
    pre_ip_headers = struct.unpack("!BBHHHBBH4s4s", payload[:20])
    ihl = (pre_ip_headers[0] & 0x0F) * 4
    ip_payloads = payload[ihl:]
    return pre_ip_headers, ip_payloads


def parse_icmp_header(icmp_data):
    icmp_headers = struct.unpack("!BBHHH", icmp_data[:8])
    icmp_payloads = icmp_data[8:]
    return icmp_headers, icmp_payloads


def parse_tcp_header(payload):
    pre_tcp_headers = struct.unpack("!HHLLBBHHH", payload[:20])
    tcp_header_length = (pre_tcp_headers[4] >> 4) * 4
    return pre_tcp_headers, payload[tcp_header_length:]


def parse_udp_header(payload):
    pre_udp_headers = struct.unpack("!HHHH", payload[:8])
    return pre_udp_headers, payload[8:]


def tcp_flags(int_num):
    return str(bin(int_num))[2:].zfill(8)


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
            ip_source_address = inet_ntoa(ip_headers[8])
            ip_destination_address = inet_ntoa(ip_headers[9])
            if ip_headers[6] == 6:  # TCP Only
                print(f"{packet_number} th packet\n")
                print(f"[TCP] {ip_source_address} => {ip_destination_address}")
                tcp_headers, tcp_payloads = parse_tcp_header(ip_payloads)
                print("Source Port: ", tcp_headers[0])
                print("Destination Port: ", tcp_headers[1])
                print("Seq Number: ", tcp_headers[2])
                print("Ack Number: ", tcp_headers[3])
                print("Offset(Length): ", tcp_headers[4] >> 4)
                print("TCP Flags: ")
                print(">> CEUAPRSF")
                print(">>", tcp_flags(tcp_headers[5]))
                print("Window Size: ", tcp_headers[6])
                print("Checksum: ", tcp_headers[7])
                print("Urgent Pointer: ", tcp_headers[8])
                print("TCP Payloads: ")
                print(tcp_payloads.decode("utf-8", "ignore"))
            elif ip_headers[6] == 17:  # UDP Only
                print(f"{packet_number} th packet\n")
                print(f"[UDP] {ip_source_address} => {ip_destination_address}")
                udp_headers, udp_payloads = parse_udp_header(ip_payloads)
                print("Source Port: ", udp_headers[0])
                print("Destination Port: ", udp_headers[1])
                print("Length: ", udp_headers[2])
                print("Checksum: ", udp_headers[3])
                print("UDP Payloads: ")
                print(udp_payloads.decode("utf-8", "ignore"))
            print("=" * 30)

    except KeyboardInterrupt:  # Ctrl-C key input
        if os.name == "nt":
            sock.ioctl(SIO_RCVALL, RCVALL_OFF)


def main():
    host = "192.168.0.5"  # 자신의 IP 주소로 변경
    print("START SNIFFING at [%s]" % host)
    parsing(host)


if __name__ == "__main__":
    main()
