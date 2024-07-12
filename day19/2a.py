def count_characters():
    with open("data.txt", 'r') as file:
        content = file.read()
        character_count = len(content)
        print("Total number of characters:", character_count)


count_characters()
