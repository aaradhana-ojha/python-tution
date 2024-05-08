# Program to demonstrate mutable and immutable objects

x = 10  # Immutable object (int)
y = [1, 2, 3]  # Mutable object (list)

choice = input("Enter 'i' for immutable or 'm' for mutable: ")

if choice == 'i':
    x += 5  # Modifying the immutable object
    print("x (immutable) after modification:", x)
elif choice == 'm':
    y.append(4)  # Modifying the mutable object
    print("y (mutable) after modification:", y)
else:
    print("Invalid choice entered.")
