# Import the necessary libraries
import os

# Create a function to get the current working directory
def get_current_directory():
  """
  This function gets the current working directory.

  Returns:
    The current working directory.
  """

  return os.getcwd()

# Create a function to change the current working directory
def change_directory(new_directory):
  """
  This function changes the current working directory.

  Args:
    new_directory: The new working directory.

  Returns:
    None.
  """

  os.chdir(new_directory)

# Create a main function
def main():
  """
  The main function.
"""

  # Get the current working directory
  current_directory = get_current_directory()

  # Print the current working directory
  print(f"Current working directory: {current_directory}")

  # Change the current working directory
  new_directory = "/path/to/new/directory"
  change_directory(new_directory)

  # Get the new current working directory
  new_current_directory = get_current_directory()

  # Print the new current working directory
  print(f"New current working directory: {new_current_directory}")

if __name__ == "__main__":
  main()
