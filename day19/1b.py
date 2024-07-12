def countlines():
    with open("data.txt","r") as f:
        x=f.readlines()
        fi=len(x)
        print(fi)
countlines()