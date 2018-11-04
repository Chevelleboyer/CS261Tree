class BinarySearchTree:
	def __init__(self, root, leftChild=None, rightChild=None):
		self.root = root

	def insertLeft(self, newNode):
		self.leftChild = newNode

	def insertRight(self, newNode):
		self.rightChild = newNode

#class TreeNode:
