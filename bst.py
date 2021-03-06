class BinarySearchTree:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, insertee):
        if insertee.value >= self.value:
        	if self.right == None:
        		self.right = insertee
        	else:
        		self.right.insert(insertee)
        if insertee.value < self.value:
        	if self.left == None:
        		self.left = insertee
        	else:
        		self.left.insert(insertee)

    def find(self, aValue):
    	if self.value == aValue:
    		return self
    	else:
            if aValue >= self.value:
                if self.right == None:
                    return None
                else:
                    return self.right.find(aValue)
            else:
                if aValue < self.value:
                    if self.left == None:
                        return None
                    else:
                        return self.left.find(aValue)

    def preOrder(self):
        values = []
        print(self.value)
        values.append(self.value)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
    
    def postOrder(self):
        values = []
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.value)
        values.append(self.value)

    def inOrder(self):
        values = []
        if self.left:
            self.left.inOrder()
        print(self.value)
        values.append(self.value)
        if self.right:
            self.right.inOrder()

    def delNode(self, nodeValue):
        if self.value == nodeValue:
            self.value = None
            self.left.parent = self.parent
        else:
            if nodeValue >= self.value:
                if self.right == None:
                    return None
                else:
                    return self.right.delNode(nodeValue)
            else:
                if nodeValue < self.value:
                    if self.left == None:
                        return None
                    else:
                        return self.left.delNode(nodeValue)

        


