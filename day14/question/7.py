def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

list_input = input("Enter a list of elements separated by spaces: ").split()
print("Reversed list:", reverse_list(list_input))
