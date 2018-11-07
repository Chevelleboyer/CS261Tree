class BinarySearchTree:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

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
    		#print(self.value, aValue)
    		return self
    	else:
    		if self.left == None & self.right == None:
    			return None
    		else:
    			if aValue >= self.value:
    				self.right.find(aValue)
    			else:
    				if aValue < self.value:
    					self.left.find(aValue)

    
    