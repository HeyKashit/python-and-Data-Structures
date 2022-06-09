def merge_sort(list):

    if len(list) <= 1:
        return list
    
    # finding mid point 
    mid =int( len(list) / 2)

    left , right  = merge_sort(list[:mid]), merge_sort(list[mid:])

    return merge(left,right)

def merge(left,right):
    result=[]
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    
    left_pointer , right_pointer = 0,0
    while(left_pointer < len(left) and right_pointer < len(right)):

        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer +=1
        
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result


print(merge_sort([1,6,3,9,10,4,5,8]))
