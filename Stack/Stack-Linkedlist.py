class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class mystack:
    def __init__(self):
        self.head=None
        self.sizee=0
    
    def push(self,x):
        temp=Node(x)
        temp.next=self.head
        self.head=temp
        self.sizee=self.sizee+1
    
    def sizen(self):
        print(self.sizee)

    
    def print_mystack(self):
        cur=self.head
        while(cur!=None):
            print(cur.data,end=" ")
            cur=cur.next

    def pop(self):
        if self.head==None:
            return "not possible"
        else:
            res = self.head.data
            self.head=self.head.next
            return res
        

m1=mystack()
m1.push(2)
m1.push(50)
m1.push(188)
m1.print_mystack()
m1.sizen()
print(m1.pop())
