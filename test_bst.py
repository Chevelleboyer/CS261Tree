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

	def test_insert_right_with_no_child(self):
		bst = BinarySearchTree(50)
		child = BinarySearchTree(70)
		bst.insertRight(child)
		self.assertEqual(child, bst.rightChild)

	def test_insert_right_with_child(self):
		pass


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