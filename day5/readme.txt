What is a Function?
A function is like a reusable recipe in Python. 
Imagine you have a recipe for making a sandwich. 
Instead of writing down all the steps every time 
you want to make a sandwich, you write the recipe 
once and then just call it whenever you need a sandwich.

Why Use Functions?
Reusability: Write the code once, use it multiple times.
Organization: Makes your code easier to read and manage.
Modularity: Breaks down a complex problem into smaller, manageable parts.


function in Python that doesn't use parameters. 
def greet():
    print("Hello! Welcome to the Python world.")

def is a keyword that tells Python you are defining a function.
greet is the name of the function.
The function doesn't have any parameters (no values inside the parentheses).
Inside the function, it simply prints a greeting message.
# Calling the function
greet()

# Output:
# Hello! Welcome to the Python world.




. Defining a Function using parameters

def make_sandwich(bread, filling):
    sandwich = bread + " sandwich with " + filling
    return sandwich

def is a keyword that tells Python you are defining a function.
make_sandwich is the name of the function.
bread and filling are inputs to the function, also called parameters.
return is a keyword that tells the function to give back the result.

sandwich1 = make_sandwich("Whole wheat", "turkey")
sandwich2 = make_sandwich("Rye", "ham and cheese")

print(sandwich1)  # Output: Whole wheat sandwich with turkey
print(sandwich2)  # Output: Rye sandwich with ham and cheese


When you call make_sandwich("Whole wheat", "turkey"), the function 
uses the inputs "Whole wheat" and "turkey", and follows the steps you defined, 
giving you a "Whole wheat sandwich with turkey".
You can call the same function with different inputs to get different results.


Another Example: Adding Two Numbers
def add_numbers(a, b):
    sum = a + b
    return sum

add_numbers is the name of the function.
a and b are the inputs (parameters).
The function adds a and b together and returns the result.

result1 = add_numbers(5, 3)
result2 = add_numbers(10, 15)

print(result1)  # Output: 8
print(result2)  # Output: 25







Built-in functions in Python are functions 
that are pre-defined and readily available 
for use without requiring explicit definition. 
These functions are part of the Python Standard 
Library and cover a wide range of tasks, from 
mathematical operations to data manipulation, 
file handling, input/output operations, and more. 

Type conversion functions in Python are built-in 
functions that allow you to convert data from one 
type to another.


input(prompt):

Used to take user input from the keyboard during program execution.
Optionally takes a prompt message (prompt) to display to the user.
Always returns a string, so type conversion may be needed for numeric inputs.
eval(expression):

Evaluates a Python expression (as a string) and returns the result.
Use with caution as it can execute arbitrary code. Avoid using it with untrusted inputs.
max(iterable, *iterables, key=None, default=None):

Returns the largest item in an iterable or among multiple iterables.
Optionally takes a key function for custom comparisons and a default value if the iterable is empty.
min(iterable, *iterables, key=None, default=None):

Returns the smallest item in an iterable or among multiple iterables.
Optionally takes a key function for custom comparisons and a default value if the iterable is empty.
abs(number):

Returns the absolute (positive) value of a number.
Works for integers, floats, and complex numbers.
type(object):

Returns the type of an object.
Useful for checking the data type of variables or objects.
name:

This doesn't refer to a specific built-in function but can be a variable storing a string value (e.g., name = "John").
len(s):

Returns the length (number of items) of an object.
Works with strings, lists, tuples, dictionaries, sets, and other iterable objects.
round(number[, ndigits]):

Rounds a floating-point number to a specified number of decimal digits (ndigits).
If ndigits is not provided, it rounds to the nearest integer.
range(start, stop[, step]):

Generates a sequence of numbers from start to stop (exclusive) with an optional step size.
Useful for creating sequences used in loops, list comprehensions, etc.





Importing modules in Python allows you to 
use code from other Python files or external 
libraries in your program. 

 import math

The random module in Python is a built-in module 
that provides functionalities related to generating 
random numbers, making random selections, and shuffling 
sequences. It is part of the Python Standard Library, 
so you can use it without installing any additional packages. more inside modules.


Factoerial
Let's use an example everyone can relate to: factorial. 
Factorial is a mathematical operation that you use to c
alculate the product of an integer and all the integers 
below it. For example, 5 factorial (written as 5!) is 5 × 4 × 3 × 2 × 1, which equals 120.

Here's how recursion helps us calculate factorial:

Base Case: Imagine you're trying to find the factorial of 1. 
Well, 1 factorial is just 1. That's our base case—it's the smallest 
version of the problem we know the answer to without any further calculation.

Recursive Case: Now, if we want to find the factorial of 
any other number, say 5, we can use recursion. We know that 5! 
is the same as 5 × 4!. But what's 4!? Well, it's 4 × 3!. And what's 
3!? It's 3 × 2!. And so on, until we reach our base case of 1!.

Stacking Up: Each time we go deeper into the recursion, 
we're essentially stacking up these smaller calculations. 
But as soon as we hit our base case (like when we reach 1!), 
we start unraveling these stacks, solving each smaller calculation until we reach the top again.

So, recursion is like a fancy way of breaking down big 
problems into smaller, more manageable ones, until we 
reach the simplest form of the problem that we already 
know how to solve. It's like solving a puzzle one piece 
at a time, with each piece being just a smaller version of the whole puzzle!

The base case is crucial in recursion. Here's why it's so important:


Stopping Condition: The base case serves as the stopping 
condition for the recursive calls. Without it, the recursive 
function would keep calling itself indefinitely, leading 
to what's known as infinite recursion. This would consume 
all available memory and eventually crash the program.

Preventing Infinite Loops: By defining a base case, 
you ensure that the recursion stops once a certain 
condition is met. This prevents the program from getting 
stuck in an infinite loop and allows it to return a result or terminate gracefully.

Determining the Result: The base case provides the result 
for the simplest form of the problem. It's the starting 
point for the recursion and often represents the solution 
to the problem when no further recursion is needed.

Guaranteeing Termination: With a base case, you 
can be confident that your recursive function will 
eventually terminate. This is essential for writing 
correct and reliable code, especially in production 
environments where unexpected crashes can have serious consequences.