
def buuble(list_a):
    sorted=False
    while not sorted:
        sorted =True
        for i in range(len(list_a)-1):
            if list_a[i] > list_a[i+1]:
                list_a[i],list_a[i+1] = list_a[i+1],list_a[i]
                sorted = False
    return list_a

def inssertion_sort(list_b):
    len_list=len(list_b)-1
    for i in range(0,len_list):
        min_index_value=i
        for j in range(i+1,len(list_b)): 
            if list_b[j]< list_b[min_index_value]:
                min_index_value= j
            if min_index_value != i:
                list_b[i],list_b[min_index_value]=list_b[min_index_value], list_b[i]
    return list_b


def quick_sort(sec):
    len_sec=len(sec)
    # check for the zero and one item array
    if len_sec <= 0:
        return sec 
    # pivot point ( Last )
    pivot=sec.pop()
    items_lower=[]
    items_high=[]
    
    # iterate over the sequence left over
    for items in sec:
        if items > pivot:
            items_high.append(items)
        else:
            items_lower.append(items)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_high)



# main function of the code
print(buuble([2,1,3,4,5,6,7,17,12]))
print(inssertion_sort([1,5,2,7,3,9,4,10,6]))
print(quick_sort([1,5,2,7,3,9,4,10,6]))
