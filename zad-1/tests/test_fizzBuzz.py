
import unittest
import json

from src.fizzBuzz import fizzBuzz



class Test_fizzBuzz(unittest.TestCase):
	def test_from_file(self):
		file = open("./fizzBuzz.json")
		testsData = json.load(file)
		file.close()
		for [input, expectedOutput] in testsData:
			self.assertEqual(fizzBuzz(input), expectedOutput)


if __name__ == "__main__":
	unittest.main()
