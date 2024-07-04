from pwn import *
import json
import codecs

conn = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = conn.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    conn.sendline(request)

def decode_response(type_val, enc_val):
    if type_val == "base64":
        return base64.b64decode(enc_val.encode()).decode()
    elif type_val == "hex":
        return bytes.fromhex(enc_val).decode()
    elif type_val == "rot13":
        return codecs.decode(enc_val, 'rot_13')
    elif type_val == "bigint":
        return bytes.fromhex(enc_val[2:]).decode()
    elif type_val == "utf-8":
        tmp = [chr(b) for b in enc_val]
        return "".join(tmp)

for i in range(100):
    response = json_recv()
    decoded_val = decode_response(response['type'], response['encoded'])
    to_send = {
        "decoded": decoded_val
    }
    json_send(to_send)

response = json_recv()
print(response['flag'])

##### BETTER SOLN #####
# d = {
#         "base64": b64d,
#         "hex": unhex,
#         "rot13": lambda s: codecs.encode(s, 'rot_13').encode(),
#         "bigint": lambda s: long_to_bytes(int(s, 0)),
#         "utf-8": bytes
# }

# def dec(o):
#     return d[o["type"]](o["encoded"])

# io = remote("socket.cryptohack.org", 13377)
# for _ in range(100):
#     o = json.loads(io.recvline())
#     io.sendline(json.dumps({"decoded": dec(o).decode()}))
# io.interactive()