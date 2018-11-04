# Run me with `python -m unittest test_bst`

import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
	"""
	Initialization
	"""
	def test_instantiation_with_value(self):
		fake_value = 27
		bst = BinarySearchTree(fake_value)
		self.assertEqual(fake_value, bst.root)

	def test_leaf_insert_smaller_values_as_left(self):
		bst = BinarySearchTree(70)
		child = BinarySearchTree(50)
		bst.insertLeft(child)
		self.assertEqual(child, bst.leftChild)

	def test_insert_right_with_child(self):
		bst = BinarySearchTree(70)
		child = BinarySearchTree(120)
		bst.insertRight(child)
		self.assertEqual(child, bst.rightChild)


	def test_instantiation(self):
		"""
		A BinarySearchTree exsists.
		"""
		try:
			BinarySearchTree(70)
		except NameError:
			self.fail("Could not instantiate BinarySearchTree")

if __name__ == '__main__':
	unittest.main()