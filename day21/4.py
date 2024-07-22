def RevString():
    
    with open("Input.txt", 'r') as file:
        content = file.read()

    words = content.split()

    for i in range(len(words)):
        if len(words[i]) > 0 and words[i][0] == 'O': 
            words[i] = words[i][::-1] 

    print(' '.join(words))


RevString()
