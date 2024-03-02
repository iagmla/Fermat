from Crypto.Util import number
import math
from rsa import keygen

# Breaks RSA with false keys

def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=True):
    a = isqrt(n)
    b2 = a*a - n
    b = isqrt(n)
    steps = 0
    while b*b != b2:
        a += 1
        b2 = a*a - n
        b = isqrt(b2)
        steps += 1
    print("steps", steps)
    p=a+b
    q=a-b
    return p, q

psize = 16
sk, pk, n = keygen(psize)
message = b"A"
msg = number.bytes_to_long(message)
p, q = fermat(n)
print(p, q)
