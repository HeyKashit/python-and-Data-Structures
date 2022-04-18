class stack:
    def __init__(self):
        self.list = []

    def push(self,data):
        self.list.append(data)
    
    def pop(self):
        self.list.pop()

    def peep(self):
        print(self.list[-1])

    def isempty(self):
        if self.list==[]:
            return "its empty"
        else:
            return "its not empty"
    
    def delete_list(self):
        self.list=None
    
    def print_list(self):
        print(self.list)
    

s1=stack()
s1.push(20)
s1.push(10)
s1.push(60)
s1.print_list()
s1.peep()
s1.pop()
s1.peep()
