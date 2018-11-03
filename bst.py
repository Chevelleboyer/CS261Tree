class BinarySearchTree:
	def __init__(self, root = None):
		self.root = root
		self.leftChild = None
		self.rightChild = None
#just do find (acess and find are very similar) find returns the total node with that value, NOT the value the node holds