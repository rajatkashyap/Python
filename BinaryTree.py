class BinaryTreeNode:
	def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

nums=[1,2,4,7,6,9,8,34]
b=BinaryTreeNode(nums[0])
for no in range(1,len(nums)):
	if nums[no]<
	