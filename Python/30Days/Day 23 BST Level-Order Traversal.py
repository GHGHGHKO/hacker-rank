import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        queue = [root]
        
        while queue:
            node_Data = queue.pop() 
            print (str(node_Data.data) + " ", end="")
            
            if node_Data.left is not None:
                queue.insert(0, node_Data.left) # insert left list
            if node_Data.right is not None:
                queue.insert(0, node_Data.right) # insert left list


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)