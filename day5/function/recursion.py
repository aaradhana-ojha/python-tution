def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: return n times the factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(5)
print("Factorial of 5 is:", result)

'''Base Case: The base case is defined by the condition 
if n == 0 or n == 1:. This checks if the value of n is 
either 0 or 1. If it is, then we know that the factorial 
of 0 or 1 is 1, so we return 1 immediately without further 
recursion. This stops the recursion from going indefinitely.

Recursive Case: If n is not 0 or 1, meaning it's a positive 
integer greater than 1, then we move to the recursive case. 
Here, we calculate the factorial of n by multiplying n with the 
factorial of (n-1). This is where the recursion occurs. 
The function calls itself with a smaller value of n, moving towards the base case.

Example: Let's say we want to find the factorial of 5 (factorial(5)). The function calls would look like this:

factorial(5) returns 5 * factorial(4) result 
factorial(4) returns 4 * factorial(3)
factorial(3) returns 3 * factorial(2)
factorial(2) returns 2 * factorial(1)
factorial(1) hits the base case and returns 1.
Then, the recursion starts unwinding:
factorial(2) receives the result of factorial(1) as 1, so it returns 2 * 1 = 2.
factorial(3) receives the result of factorial(2) as 2, so it returns 3 * 2 = 6.
factorial(4) receives the result of factorial(3) as 6, so it returns 4 * 6 = 24.
factorial(5) receives the result of factorial(4) as 24, so it returns 5 * 24 = 120.'''


#https://www.youtube.com/watch?v=TqqQld6m6A0&t=192s