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

	def test_leaf_insert_larger_values_as_right(self):
		bst = BinarySearchTree(70)
		child = BinarySearchTree(120)
		bst.insertRight(child)
		self.assertEqual(child, bst.rightChild)

	def test_nonLeaf_insert_smaller_value_as_left(self):
		bst = BinarySearchTree(70)
		child = BinarySearchTree(50)
		bst.insertLeft(child)
		child2 = BinarySearchTree(25)
		bst.insertLeft(child)

	def test_finding_value_smaller_than_root(self):
		bst = BinarySearchTree(70)
		bst2 = BinarySearchTree(50)
		bst3 = BinarySearchTree(100)
		bst.insertLeft(bst2)
		bst.insertRight(bst3)
		bst.find(17)


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