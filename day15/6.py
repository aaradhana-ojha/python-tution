'''A binary file "SHOP.DAT" has structure [ITEM_number, ITEM_Name, Qty]. Write a function countrec() in Python that would read contents of the file "SHOP.DAT" and display the details of those items whose qty is more than 45.'''
import pickle

def countrec():
    with open("SHOP.DAT", "rb") as f:
        try:
            while True:
                record = pickle.load(f)
                if record[2] > 45:
                    print(record)
        except EOFError:
            pass

# Example usage
countrec()
