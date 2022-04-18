class Node:
	def __init__(self,value):
		self.key=value
		self.next=None

def print_linked_list(head):
	curr=head
	while(curr!=None):
		print(curr.key,end=" ")
		curr=curr.next
      
def search(head,x):
	pos=0
	curr=head
	while(curr!=None):
		if curr.key==x:
			return pos
		pos=pos+1
		curr=curr.next
	return -1

def insert_at_head(head,x):
	temp=Node(x)
	temp.next=head
	return temp


def inster_at_end(head,x):
	curr=head
	if head == None:
		return Node(x)
	while(curr.next!=None):
		curr=curr.next
	curr.next=Node(x)
	return head

# insert at any position
def at_any_position(head,pos,x):
	if pos==1:
		temp=Node(x)
		temp.next=head
		return temp
	curr=head
	for i in range (pos-2):
		curr=curr.next
		if curr == None:
			return head
	temp=Node(x)
	temp.next = curr.next
	curr.next=temp
	return head
# delete at the front
def delet_front(head):
	pass
# Driver code
head=Node(10)
head=insert_at_head(head,20)
head=insert_at_head(head,100)
head=insert_at_head(head,60)
head=insert_at_head(head,30)
head=inster_at_end(head,9999)
head=at_any_position(head,2,88888888)
print_linked_list(head)
print("  search ")	
ans=search(head,10)	
print(ans)
