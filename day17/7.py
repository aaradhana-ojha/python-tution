import pickle

def CountRec(author):
    with open('Book.dat', 'rb') as file:
        count = 0
        while True:
            try:
                book = pickle.load(file)
                if book['Author'] == author:
                    count += 1
            except EOFError:
                break
        return count

