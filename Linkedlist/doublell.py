class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doublell:
    def __init__(self):
        self.head=None
    
    def insert_head(self,data):
        if(self.head==None):
            newNode=Node(data)
            self.head=newNode
            newNode.prev=None
        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode
            newNode.prev=None
            x=newNode.next
            x.prev=newNode
            
        
    def print(self):
        curr=self.head
        while(curr):
            print(curr.data,end=" ")
            curr=curr.next
        
            
        
d1=doublell()
d1.insert_head(20)
d1.insert_head(10)
d1.insert_head(7)
d1.insert_head(1)
d1.print()
