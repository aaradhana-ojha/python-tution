def rotate_list(lst):
    if len(lst) <= 1:
        return lst
    return lst[1:] + [lst[0]]

list_input = input("Enter a list of elements separated by spaces: ").split()
print("Rotated list:", rotate_list(list_input))
