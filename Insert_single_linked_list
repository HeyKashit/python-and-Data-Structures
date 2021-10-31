class Node:
	def __init__(self,k):
		self.key=k
		self.next=None

def print1(head):
	curr=head
	while(curr!=None):
		print(curr.key, end = " ")
		curr=curr.next

def insert(head,val):
	temp=Node(val)
	temp.next=head
	return temp


temp1=Node(40)
temp2=Node(55)
temp1.next=temp2
head=temp1
head = insert(head,10)
head = insert(head,20)
print1(head)
