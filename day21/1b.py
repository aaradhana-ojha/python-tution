def RevString():
    with open('file.txt', 'r') as file:
        content = file.read()
        words = content.split()
        for i in range(len(words)):
            if i % 2 != 0:
                words[i] = words[i][::-1]
        print(' '.join(words))


RevString()
