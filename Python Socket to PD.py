import socket
import time

s = socket.socket()
host = socket.gethostname()
#choose port number
port = #num#
s.connect((host, port))
print("setup complete")
scale = 200
scale_inc = 1

def pdsend(pd_value):
    val4str = str(pd_value)
    ba4 = bytes(val4str, 'utf8')
    s.sendall(ba4)
    s.sendall(b';')
    time.sleep(.01)

while True:
    scale = (scale + scale_inc)
    if scale <= 200: scale_inc = 1
    if scale >= 500: scale_inc = -1
    pdsend(scale)
    print(scale)





