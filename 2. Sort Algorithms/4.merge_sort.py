def merge(left_list, right_list):
    combined = []
    i=0
    j=0
    while i < len(left_list) or j < len(right_list):
        if  j >= len(right_list):
            combined.append(left_list[i])
            i+=1
        elif i >= len(left_list):
            combined.append(right_list[j])
            j+=1
        elif left_list[i] < right_list[j]:
            combined.append(left_list[i])
            i+=1
        else:
            combined.append(right_list[j])
            j+=1
    
    return combined


def merge_sort(elements):
    if len(elements) == 1:
        return elements
    
    mid_index = len(elements)//2
    left = merge_sort(elements[:mid_index])
    right = merge_sort(elements[mid_index:])
    
    return merge(left, right)

print(merge_sort([4,2,6,5,1,3]))