def buuble_sort(sequence):
    length=len(sequence) -1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0,length):
            if sequence[i]> sequence[i+1]:
                sorted = False
                sequence[i],sequence[i+1]=sequence[i+1],sequence[i]
    
    return sequence


arr=[1,2,2,22,4,5,6,7,8,55,44,33,23,1,23,0,9,8,7,6,9898]
print(buuble_sort(arr))
