S= "kashit"
from collections import deque
s=deque()
index = 0
while(index<len(S)):
    character = S[index]
    s.append(character)
    index = index +1

#print(s)
    
index1=0
ans=""
while(index1<len(s)):
    character = s.pop()
    print(character)
        
    ans=ans+str(character)
    index = index+1
print(ans)
    
