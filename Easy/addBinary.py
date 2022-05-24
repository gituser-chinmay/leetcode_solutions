class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #Typecasting strings to int with base 10 gives decimal, bin converts sum back into binary,
        #first two characters sliced as they are '0b'
        return bin(int(a,2)+int(b,2))[2:]
