#Flow of Execution:
# Flow of execution refers to the order in which statements in a program are executed.
# It starts from the top of the program and proceeds sequentially unless altered by control flow statements.
#code:
def firstPrint():
    print("First")
    secondPrint()
	
def secondPrint():
    print("Second")
    thirdPrint()
	
def thirdPrint():
    print("Third")
	
firstPrint()