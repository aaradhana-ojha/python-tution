def create_file(filename, content):
  """
  Creates a text file with the given filename and saves the provided content in it.

  Args:
      filename (str): The name of the text file to create.
      content (str): The content to be saved in the file.
  """
  # Open the file in write mode ('w') to create or overwrite the content
  with open(filename, 'w') as file:
    file.write(content)
  print("File '%s' created successfully." % filename)  # Traditional string formatting

def read_file(filename):
  """
  Reads the content from a text file with the given filename and displays it.

  Args:
      filename (str): The name of the text file to read from.
  """
  try:
    # Open the file in read mode ('r')
    with open(filename, 'r') as file:
      content = file.read()
    print("Content of '%s':" % filename)  # Traditional string formatting
    print(content)
  except FileNotFoundError:
    print("Error: File '%s' not found." % filename)  # Traditional string formatting

# Example usage
content_to_save = "This is some sample content for myfile.txt."
create_file("myfile.txt", content_to_save)

read_file("myfile.txt")
