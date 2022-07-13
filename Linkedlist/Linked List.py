class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlylinked:
    def __init__(self):
        self.head=None
        
    def print(self):
        curr=self.head
        while(curr):
            print(curr.data,end=" ")
            curr=curr.next
        print()
        
    def insert_head(self,data):
        if self.head == None:
            newNode = Node(data)
            self.head=newNode
        else:
            newNode = Node(data)
            newNode.next=self.head
            self.head=newNode
            
    def insert_end(self,data):
        if self.head==None:
            newNode = Node(data)
            self.head=newNode
        else:
            curr=self.head
            newNode=Node(data)
            while(curr.next!=None):
                curr=curr.next
            
            curr.next=newNode
            
    def nth(self,key):
        if(self.head==None):
            print("not possible")
        curr=self.head
        for i in range(key):
            curr=curr.next
            i+=1
        prev=self.head
        while(curr):
            curr=curr.next
            prev=prev.next
        print(prev.data)
    
    
    def duplicates1(self):
        curr=self.head
        prev=None
        duplicate_value=dict()
        while(curr!=None):
            if curr.data in duplicate_value:
                prev.next=curr.next
                curr=None
            else:
                duplicate_value[curr.data]=1
                prev=curr
            curr=curr.next
                
        
            
                
            
    def delete_head(self):
        if(self.head == None):
            print(" Not possible")
        else:
            data = self.head.data
            self.head=self.head.next
            print(str(data)+" deleted")
        
    def delete_end(self):
        if self.head == None:
            print("Not Possible")
        else:
            curr=self.head
            prev=None
            while(curr.next!=None):
                prev=curr
                curr=curr.next
        prev.next=None
        
    def search(self,key):
        if self.head == None:
            return False
        else:
            curr=self.head
            while(curr):
                if(curr.data == key):
                    return True
                curr=curr.next
            return False
    
    def reverse(self):
        if self.head == None:
            print("Not possible")
        else:
            prev=None
            curr=self.head
            while(curr!=None):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            self.head=prev
            
        
            
        

l1=singlylinked()
l1.insert_head(10)
l1.insert_head(6)
l1.insert_head(3)
l1.insert_head(100)
l1.insert_end(32)
l1.insert_end(33)
l1.print()
l1.delete_head()
l1.print()
l1.delete_end()
l1.print()
print(l1.search(32))
l1.reverse()
l1.print()
l1.insert_mid(234,3)
l1.print()
l1.insert_end(10)
