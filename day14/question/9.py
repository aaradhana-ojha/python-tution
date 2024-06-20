def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

content = input("Enter content to save in myfile.txt: ")
create_file('myfile.txt', content)
print("Content of myfile.txt:")
print(read_file('myfile.txt'))
