def print_alternate_elements(lst):
    return lst[::2]

list_input = input("Enter a list of elements separated by spaces: ").split()
print("Alternate elements:", print_alternate_elements(list_input))
