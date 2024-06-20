def exchange_first_last(s):
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]

string_input = input("Enter a string: ")
print("New string:", exchange_first_last(string_input))
