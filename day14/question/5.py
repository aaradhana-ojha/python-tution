def print_initials(name):
    initials = []
    words = name.split()
    for word in words:
        initials.append(word[0].upper() + '.')
    return ' '.join(initials)

name_input = input("Enter your full name: ")
print("Initials:", print_initials(name_input))
