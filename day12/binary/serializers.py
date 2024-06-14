import pickle

# Serialize the data
favorite_books = ["Alice in Wonderland", "1984", "To Kill a Mockingbird"]
with open('books.pkl', 'wb') as file:
    pickle.dump(favorite_books, file)

print("Data has been serialized and saved to 'books.pkl'.")

# Deserialize the data
with open('books.pkl', 'rb') as file:
   # loaded_books = pickle.load(file)
    print("Data loaded from 'books.pkl':")
    print(pickle.load(file))
