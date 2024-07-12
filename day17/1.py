BigNums = []

def PushBig(nums):
    for num in nums:
        if len(str(num)) >= 5:
            BigNums.append(num)

def PopBig():
    while BigNums:
        print(BigNums.pop())
    print("Stack Empty")


nums = [213, 10025, 167, 254923, 14, 1297653, 31498, 386, 92765]
PushBig(nums)
PopBig()
