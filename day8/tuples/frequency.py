def count_frequency(tup):
    frequency_dict = {}
    for element in tup:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    return frequency_dict

# Example tuple
elements = (10, 20, 30, 20, 10, 10, 40, 50, 50, 50)

# Counting frequency of elements
frequency = count_frequency(elements)
print(frequency)
