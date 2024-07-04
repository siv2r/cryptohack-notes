# The `repr()` representation of a `bytes` object will always use ASCII printable characters and short one-letter escape sequences where possible. See [this thread](https://stackoverflow.com/questions/40983146/why-does-bytes-fromhex-treat-some-hex-values-strangely)

# hex strings to bytes
hstr = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
flag1 = bytes.fromhex(hstr)

# integers to bytes
int_val = 0x63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
len2 = (len(hstr) + 1) // 2
len3 = (len(hex(int_val)[2:]) + 1) // 2 # len(hex(int_val)) will count '0x' also, hence exclude the first two chars
assert len2 == len3
flag2 = int.to_bytes(int_val, len2, byteorder="big")
# another way
flag3 = bytes.fromhex(hex(int_val)[2:])
assert flag2 == flag3

# bytes to base64
import base64
hstr = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bstr = bytes.fromhex(hstr)
flag = base64.b64encode(bstr)

# int (msg) to ascii char (msg)
imsg = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
hmsg = hex(imsg)[2:]
bmsg1 = bytes.fromhex(hmsg)
msg = bmsg1.decode('ascii')
# or use `long_to_bytes()` method from PyCryptodome
from Crypto.Util.number import *
bmsg2 = long_to_bytes(imsg)

# XOR string & int
string = "label"
res_ord = [ord(ch) ^ 13 for ch in string]
res = [chr(i) for i in res_ord]
flag1 = "".join(res)
# or use `pwntools` module xor() function that can XOR together data of different types and lengths
# by default the xor function make both its arg equal length, by repeating the shorter arg several times
import pwn
flag2 = pwn.xor(string.encode('ascii'), 13) # encode str to bytes before XORing



