#SINGLE BYTE XOR CIPHER

def hexxor(a,b):
    a= bytes.fromhex(a)
    b= bytes.fromhex(b)
    return bytes([p ^ q for p,q in zip(a,b)])

def getScore(check):
    freq= {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    return sum([freq.get(chr(byte),0) for byte in check.lower()])

ciphertxt= "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
len= len(bytes.fromhex(ciphertxt))

maxScore= 0.
message= ''
bestKey= ''

for i in range(256):
    byte= i.to_bytes(1,'big')

    test= b''
    for j in range(len):
        test= test+byte
    
    check= hexxor(test.hex(),ciphertxt)
    score= getScore(check)

    if(maxScore<score):
        maxScore= score
        message= check.decode()
        bestKey= byte

print("Best Message: "+message)
print("Score       : "+str(maxScore))
print("Possible Key: "+str(bestKey))