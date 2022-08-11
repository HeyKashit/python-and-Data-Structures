def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)
    
    
A = ['t','u','t','o','r','i','a','l']
for i in range(len(A)):
   min_= i
   for j in range(i+1, len(A)):
      if A[min_] > A[j]:
         min_ = j
   #swap
A[i], A[min_] = A[min_], A[i]
# main
for i in range(len(A)):
   print(A[i])
