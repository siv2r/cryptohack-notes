# Cryptohack FAQ: https://cryptohack.org/faq/#netcat
# Connections with pwntools: https://es7evam.gitbook.io/security-studies/exploitation/sockets/03-connections-with-pwntools

from pwn import * # pip install pwntools
import json

HOST = "socket.cryptohack.org"
PORT = 11112

conn = remote(HOST, PORT)


def json_recv():
    line = conn.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    conn.sendline(request)


print(conn.readline())
print(conn.readline())
print(conn.readline())
print(conn.readline())

request = {
    "buy": "flag"
}
json_send(request)

response = json_recv()

print(response)