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

    def getHeight(self,root):
        #Write your code here
        if root != None:
            left_Path = self.getHeight(root.left) + 1
            #print('left_Path', left_Path, root)
            right_Path = self.getHeight(root.right) + 1
            #print('right_Path', right_Path, root)
            return max(left_Path, right_Path)
        else:
            #print('else', -1, root)
            return -1
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input()) # 3 5 2 1 4 6 7
    root=myTree.insert(root,data)
height=myTree.getHeight(root) # root 3
print(height)       