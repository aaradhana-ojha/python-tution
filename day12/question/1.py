'''You are developing a feature for a Python 
application that needs to save user settings 
across sessions. The user settings are stored 
in a dictionary where keys are the setting 
names and values are the user's preferences. 
You are tasked with writing the code to serialize 
this dictionary to a file and then deserialize it 
back into a dictionary for use when the application restarts.'''

import pickle


user_settings = {
    "theme": "dark",
    "notifications": True,
    "language": "English"
}

with open('settings.pkl', 'wb') as file:
    pickle.dump(user_settings, file)
    print("Data has been serialized and saved to 'settings.pkl'.")


with open('settings.pkl', 'rb') as file:
        loaded_settings = pickle.load(file)
        print("Data loaded from 'settings.pkl':")
        print(loaded_settings)
