a = 15
y = 12

def myfunc():
    global a
    y = a
    a = 2
    print("y=", y, "a=", a)
    print("a+y=", a + y)
    return a + y

print("y=", y, "a=", a)
print(myfunc())
print("y=", y, "a=", a)
