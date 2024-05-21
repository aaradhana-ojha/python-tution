def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The GCD of", num1, " and ", num2, " is",gcd(num1, num2))

if __name__ == "__main__":
    main()
