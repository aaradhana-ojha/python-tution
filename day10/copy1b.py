try:
    # Add content to file A (create if it doesn't exist)
    with open('file_AA.txt', 'w') as file_A:  # Use 'w' for creating or overwriting
        content_to_add = "This is the new content added to file A.\n"  # Replace with your desired content
        file_A.write(content_to_add)

    # Open file A for reading
    with open('file_AA.txt', 'r') as file_A:
        data = file_A.read()

    # Create file B (if it doesn't exist) and open it for writing
    with open('file_BB.txt', 'w') as file_B:
        file_B.write(data)

    print("Data copied successfully from file A to file B.")

    # Open file B for reading and print its content (optional)
    with open('file_BB.txt', 'r') as file_B:
        print("Content of file B:")
        print(file_B.read())

except FileNotFoundError:
    print("File AA does not exist. Created a new file AA with the provided content.")

except Exception as e:
    print("An unexpected error occurred:", e)
