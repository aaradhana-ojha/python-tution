def min_max_mean(tup):
    min_val = min(tup)
    max_val = max(tup)
    mean_val = sum(tup) / len(tup)
    return min_val, max_val, mean_val

# Example tuple
values = (10, 20, 30, 40, 50)

# Finding min, max, mean
min_val, max_val, mean_val = min_max_mean(values)
print("Minimum:", min_val, "Maximum:", max_val, "Mean:", mean_val)
