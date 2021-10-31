Class Node:
	def __init__(self,k):
		self.key=k
		self.next=None

# print linked list function.
def print_list(head):
	curr = head
	while (curr != None):
		print(curr.key, end=" ")
		curr= curr.next


# Driver code.
temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)

temp1.next =temp2
temp2.next =temp3
head=temp1

print_list(head)
