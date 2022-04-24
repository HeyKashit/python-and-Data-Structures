def quicksort(sequence):
    length=len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    itemlower=[]
    itemhiger=[]

    for items in sequence:
        if items < pivot:
            itemlower.append(items)
        else:
            itemhiger.append(items)
        
    return quicksort(itemlower) + [pivot] + quicksort(itemhiger)

arrr=[1,2,3,4,3,2,1,2,33,44,34,22,12,32,456,87,555,6,7,7,888,76,6,75,0]
print(quicksort(arrr))
