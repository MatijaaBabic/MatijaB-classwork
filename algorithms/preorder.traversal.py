class TreeNode():
    def __init__(self, data,left=-1,right=-1) -> None:
        self.left = left
        self.data = data
        self.right = right
    #end constructor
    def __repr__(self) -> str:
        return 'Right:' + str(self.right) + '\nData:' + str(self.data) + '\nLeft:'+ str(self.left)
    #end function
#end class
def inOrderTraverse(p):
    if tree[p].left != -1: #then 
        inOrderTraverse(tree[p].left) 
    #endif 
    print(tree[p].data) 
    if tree[p].right != -1: #then
        inOrderTraverse(tree[p].right)
    #endif 
#end procedure
tree = []
tree.append(TreeNode(10,1,3))
tree.append(TreeNode(5,2,5))
tree.append(TreeNode(3))
tree.append(TreeNode(23,6,4))
tree.append(TreeNode(34))
tree.append(TreeNode(8))
tree.append(TreeNode(17))
inOrderTraverse(0)