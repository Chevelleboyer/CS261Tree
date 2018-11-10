# Run me with `python -m unittest test_bst`

import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

	def test_instantiation(self):
		"""
		A BinarySearchTree exsists.
		"""
		try:
			BinarySearchTree()
		except NameError:
			self.fail("Could not instantiate BinarySearchTree")

	def test_tree_node_initial_value_none(self):
		bst = BinarySearchTree()
		self.assertEqual(None, bst.value)

	def test_tree_node_initial_value(self):
		bst = BinarySearchTree(50)
		self.assertEqual(50, bst.value)

	def test_tree_node_has_left_and_right_initially_none(self):
		bst = BinarySearchTree()
		self.assertEqual(None, bst.left)
		self.assertEqual(None, bst.right)

	def test_insert_smaller_into_single_level_tree(self):
		bst = BinarySearchTree(50)
		insertee = BinarySearchTree(25)
		bst.insert(insertee)
		self.assertEqual(insertee, bst.left)

	def test_insert_larger_into_single_level_tree(self):
		bst = BinarySearchTree(50)
		insertee = BinarySearchTree(75)
		bst.insert(insertee)
		self.assertEqual(insertee, bst.right)

	def test_insert_smaller_into_two_level_tree(self):
		bst = BinarySearchTree(50)
		insertee1 = BinarySearchTree(40)
		insertee2 = BinarySearchTree(25)
		bst.insert(insertee1)
		bst.insert(insertee2)
		self.assertEqual(insertee2, bst.left.left)

	def test_insert_larger_into_two_tree_level(self):
		bst = BinarySearchTree(50)
		insertee1 = BinarySearchTree(75)
		insertee2 = BinarySearchTree(100)
		bst.insert(insertee1)
		bst.insert(insertee2)
		self.assertEqual(insertee2, bst.right.right)

	#def test_find_when_only_one_node(self):
	#	bst = BinarySearchTree(50)
	#	bst.find(50)
	#	self.assertEqual(bst.find(50), bst.value)

	def test_find_with_two_level_tree(self):
		bst = BinarySearchTree(50)
		insertee1 = BinarySearchTree(25)
		insertee2 = BinarySearchTree(75)
		bst.insert(insertee1)
		bst.insert(insertee2)
		bst.find(75)
		self.assertEqual(bst.find(75), bst.right)

	def test_traverseInOrder_with_single_level_tree(self):
		bst = BinarySearchTree(25)
		self.assertEqual(bst.traverseInOrder(), 25)




if __name__ == '__main__':
	unittest.main()