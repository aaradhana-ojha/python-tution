#upper, lower, digit, blank count
def count(n):
    lower=0
    upper=0
    digit=0
    blank=0    
    for i in n:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
        elif i.isdigit():
            digit+=1
        elif i==" ":
            blank+=1
    return lower,upper,digit,blank
n=input("Enter")



print(count(n))
