'''You are developing an application that 
processes image data and needs to temporarily 
store these images in a binary format. You must 
write Python code to save an image's binary data to a 
file and then read it back for processing.'''

# Save the image data to a binary file
import pickle

# Save the image data to a binary file using pickle
with open('input.jpg', 'rb') as file:
    image_data = file.read()

with open('image.bin', 'wb') as file:
    pickle.dump(image_data, file)  # Use pickle to serialize the binary data

# Retrieve the image data from the binary file using pickle
with open('image.bin', 'rb') as file:
    loaded_image_data = pickle.load(file)  # Use pickle to deserialize the binary data

with open('output.jpg', 'wb') as file:
    file.write(loaded_image_data)

print("Image data has been successfully retrieved and stored in 'output.jpg'.")
