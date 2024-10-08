from Crypto.Cipher import DES
import random
from Crypto.Util.Padding import pad, unpad
import time


'''
## Solve

It is a Meet-in-the-Middle attack. No knowledge on DES insides is required.
ECB is the simplest block cipher mode vulnerable to many known plaintexts attacks.

Basically, we apply a smart bruteforce on the known (plain,enc) couple using a divide & conquer approach in order to find the 4 keys.

Each generated key are derivated from a 11 bit int which implies (2^11)^4 bits possible for k=k1||k2||k3||k4 .
Let n = 11 possible bits for 1 key.

Instead of bruteforce (2^n)^4 keys we generate each possible ENC2(ENC1(plain)) and DEC3(DEC4(enc)) seeking for a unique match (using random keys, and because of the symmetry, both loops are identical).
So we compute 2*(2^(2n)) bits (2 list of 2n bits lengths keys k1||k2 and k2||k4) and search for the intersection.

If we use m = 4n the lenght for k=k1||k2||k3||k4 we compute the keys in O(2^(m/2)) instead of O(2^m) which is considerable.
The we recover the flag using the found keys.

a, b, c, d = b'01470147' b'19111911' b'18481848' b'13321332'
'''
enc_flag = "1b15e71f37951e9950123c599921985e410be6aeb076cf5ebeac6810cce9bc06fcf07d6e4f33a1aa3c94dd00945dc96e"
enc = "cf5fca567b2713cd288489671866baae"


plain = b"pl@1ntxt"
enc = bytes.fromhex(enc)
start = time.time()

l_enc = {}
l_dec = {}
for k1 in range(2048):
    key_a = (str(k1).zfill(4)*3)[:8].encode()
    for k2 in range(2048):
        key_b = (str(k2).zfill(4)*3)[:8].encode()
        cipher_a = DES.new(key_a, mode=DES.MODE_ECB)
        cipher_b = DES.new(key_b, mode=DES.MODE_ECB)
        ct = cipher_a.encrypt(pad(plain, 8))
        ct = cipher_b.encrypt(ct)
        l_enc[ct] = [(k1, k2)]

for k1 in range(2048):
    key_c = (str(k1).zfill(4)*3)[:8].encode()
    for k2 in range(2048):
        key_d = (str(k2).zfill(4)*3)[:8].encode()
        cipher_c = DES.new(key_c, mode=DES.MODE_ECB)
        cipher_d = DES.new(key_d, mode=DES.MODE_ECB)
        dec = cipher_d.decrypt(enc)
        dec = cipher_c.decrypt(dec)
        l_dec[dec] = [(k1, k2)]

s1 = set(l_enc)
s2 = set(l_dec)
intersection = list(s1 & s2)
print(intersection)
ind = intersection[0]
#print(l_dec[ind])
for x in l_enc[ind]:    
    (seed_a, seed_b) = x
    for y in l_dec[ind]:
        (seed_c, seed_d) = y
        key_a, key_b, key_c, key_d = (str(seed_a).zfill(4)*3)[:8].encode(), (str(seed_b).zfill(4)*3)[:8].encode(), (str(seed_c).zfill(4)*3)[:8].encode(), (str(seed_d).zfill(4)*3)[:8].encode()
        print(key_a, key_b, key_c, key_d)
        cipher_a = DES.new(key_a, mode=DES.MODE_ECB)
        cipher_b = DES.new(key_b, mode=DES.MODE_ECB)
        cipher_c = DES.new(key_c, mode=DES.MODE_ECB)
        cipher_d = DES.new(key_d, mode=DES.MODE_ECB)
        flag = cipher_a.decrypt(cipher_b.decrypt(cipher_c.decrypt(cipher_d.decrypt(bytes.fromhex(enc_flag)))))
        print(flag)
        end = time.time()
        print("[+] Time elapsed:", end-start)
