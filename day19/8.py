def count_and_display_articles(filename):
    article_count = 0
    with open(filename, 'r') as file:
        for line in file:
            
            words = line.strip().split()
            
            if words and words[0].lower() in ['a', 'an', 'the']:
                print(line.strip())  
                article_count += 1

    print("Total number of lines starting with an article:", article_count)


filename = 'data.txt'  
print("Lines starting with an article (a, an, the):")
count_and_display_articles(filename)
