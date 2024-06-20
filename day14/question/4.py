def shift_left(s):
    if len(s) <= 1:
        return s
    return s[1:] + s[0]

string_input = input("Enter a string: ")
print("New string:", shift_left(string_input))
