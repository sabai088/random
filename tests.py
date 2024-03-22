import unittest

from randomizer import generate_random_number

class TestRandomizer(unittest.TestCase):

  def test_generate_random_number_in_range(self):
    """
    This test ensures that the `generate_random_number` function generates a number within the specified range.
    """

    # Set the range
    min_value = 1
    max_value = 100

    # Generate a random number
    random_number = generate_random_number(min_value, max_value)

    # Check that the random number is within the range
    self.assertGreaterEqual(random_number, min_value)
    self.assertLessEqual(random_number, max_value)

if __name__ == "__main__":
  unittest.main()
