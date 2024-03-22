import random

def generate_random_number(min_value, max_value):
  """
  This function generates a random number within a given range.

  Args:
    min_value: The minimum value.
    max_value: The maximum value.

  Returns:
    A random number within the range [min_value, max_value].
  """

  return random.randint(min_value, max_value)

def main():
  """
  The main function.
  """

  # Set the range
  min_value = 1
  max_value = 100

  # Generate a random number
  random_number = generate_random_number(min_value, max_value)

  # Print the result
  print(f"Random number: {random_number}")

if __name__ == "__main__":
  main()
