#This solution takes lesser time but more space
#Another approach is to compare the letters and subtract if a matching condition is obtained

def romanToInt(self, s: str) -> int:
    CONVERSION = {
        'I':1,
        'A':4,
        'V':5,
        'B':9,
        'X':10,
        'E':40,
        'L':50,
        'F':90,
        'C':100,
        'G':400,
        'D':500,
        'H':900,
        'M':1000
    }
    
    num = 0
    s = s.replace('IV','A')
    s = s.replace('IX','B')
    s = s.replace('XL','E')
    s = s.replace('XC','F')
    s = s.replace('CD','G')
    s = s.replace('CM','H')
                  
    
    for letter in s:
        num += CONVERSION[letter]
                        
    return num
                        

if __name__ == '__main__':
    print(romanToInt('III'))