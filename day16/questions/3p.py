# Using double backslash to include a literal backslash in a string
path = "C:\\Users\\Name\\Documents"
print("Path with double backslashes:", path)

# Using escape sequences for special characters
newline_example = "Hello\\nWorld"  # This will print the string with literal \n
print("String with literal \\n:", newline_example)

# Correct usage to actually create a new line
correct_newline_example = "Hello\nWorld"
print("String with newline:\n", correct_newline_example)

# Using raw strings to avoid escaping backslashes
raw_path = r"C:\Users\Name\Documents"
print("Raw string path:", raw_path)

# Escaping quotes within a string
quote_example = "He said, \"Hello!\""
print("String with escaped quotes:", quote_example)

# Using Unicode characters
unicode_example = "Copyright symbol: \u00A9"
print("String with Unicode character:", unicode_example)
