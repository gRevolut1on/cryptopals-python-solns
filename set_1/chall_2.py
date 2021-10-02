#FIXED XOR (for hexstrings)

def hexxor(a,b):
    a= bytes.fromhex(a)
    b= bytes.fromhex(b)
    return bytes([p ^ q for p,q in zip(a,b)]).hex()

s1= "1c0111001f010100061a024b53535009181c"
s2= "686974207468652062756c6c277320657965"

print(hexxor(s1,s2))