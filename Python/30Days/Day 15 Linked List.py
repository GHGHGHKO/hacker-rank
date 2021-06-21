class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
class Solution: 
    def display(self,head):
        current = head
        while current: # None -> End
            print(current.data,end=' ')
            current = current.next # Next data

    def insert(self,head,data): 
    #Complete this method
        if head is None:
            head = Node(data) # First data
        
        else:
            current = head 
            while current.next: # None -> End
                current = current.next
                
            current.next = Node(data) # None <= insert data
            
        return head
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
    
mylist.display(head); 	  