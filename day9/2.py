#vowel count
def countvowel(n):
    c=0
    vowel="AEIOUaeiou"
    for i in n:
        if i in vowel:
            c=c+1
    return c
n="helooworld"
print(countvowel(n))