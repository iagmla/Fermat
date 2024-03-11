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

def zfermat(n, verbose=True):
    a = isqrt(n)
    if a % 2 == 0:
        a += 1
    while (n % a) != 0:
        a += 2
    p = a
    q = n // p
    return p, q

psize = 16
sk, pk, n = keygen(psize)
message = b"A"
msg = number.bytes_to_long(message)
p, q = zfermat(n)
print(p, q)
