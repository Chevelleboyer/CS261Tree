# Run me with `python -m unittest test_bst`

import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
	"""
	Initialization
	"""
	def test_instantiation_with_value(self):
		fake_value = "Fake"
		bst = BinarySearchTree(fake_value)
		self.assertEqual(fake_value, bst.value)

	def test_instantiation(self):
		"""
		A BinarySearchTree exsists.
		"""
		try:
			BinarySearchTree()
		except NameError:
			self.fail("Could not instantiate BinarySearchTree")

if __name__ == '__main__':
	unittest.main()