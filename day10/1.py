# Writing to the file
file = open("file.txt", "w")
file.write("Hello World\n")
file.write("This is a second line.\n")
file.close()

# Reading the entire content of the file
file = open("file.txt", "r")
content = file.read()
print("Reading entire content using read():")
print(content)
file.close()

# Reading the file line by line
file = open("file.txt", "r")
print("Reading line by line using readline():")
print(file.readline(), end='')  # Read first line
print(file.readline(), end='')  # Read second line
file.close()


'''file mode 
r- read
w- write
a- append
r+- read and write
w+- write and read
b- binary'''

'''file operations
create
read
write
copy
delete
close'''