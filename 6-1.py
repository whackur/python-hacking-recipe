import whois  # pip install python-whois
import socket

url = "hakhub.net"

try:
    url_info = whois.whois(url)
    ip = socket.gethostbyname(url)
    print("=" * 50)
    print("<< URL Info >>")
    print(url_info)
    ip_info = whois.whois(ip)
    print("=" * 50)
    print("<< IP Info >>")
    print(ip_info)
except whois.parser.PywhoisError:
    print("Unregistered")
