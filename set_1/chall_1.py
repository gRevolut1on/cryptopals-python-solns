#CONVERT HEX TO BASE64 (and vice versa)

from base64 import b64decode, b64encode

def hex2base64(str):
    return b64encode(bytes.fromhex(str)).decode()

def base642hex(str):
    return b64decode(base).hex()

inp= "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base= "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
print(hex2base64(inp))
print(base642hex(base))