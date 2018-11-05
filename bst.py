class BinarySearchTree:
	def __init__(self, root, left=None, right=None):
		self.root = root
		self.leftChild = left
		self.rightChild = right

	#def insertLeft(self, newNode):
		#self.leftChild = newNode

	#def insertRight(self, newNode):
		#self.rightChild = newNode

	def put(self,key,val):
    	if self.root:
        	self._put(key, val, self.root)
    	else:
        	self.root = TreeNode(key, val)
    	self.size = self.size + 1

	def _put(self, key, val, currentNode):
    	if key < currentNode.key:
        	if currentNode.hasLeftChild():
               self._put(key, val, currentNode.leftChild)
        	else:
               currentNode.leftChild = TreeNode(key, val, parent = currentNode)
    	else:
        	if currentNode.hasRightChild():
               self._put(key, val, currentNode.rightChild)
        	else:
               currentNode.rightChild = TreeNode(key, val, parent = currentNode)



class TreeNode:
   def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def __iter__(self):
   		if self:
      		if self.hasLeftChild():
      			for elem in self.leftChiLd:
                	yield elem
      		yield self.key
      		if self.hasRightChild():
             	for elem in self.rightChild:
                	yield elem




