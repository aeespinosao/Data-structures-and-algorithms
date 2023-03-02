def quick_sort(elements):
    
    if len(elements) <= 1:
        return elements
    
    pivot = elements[0]
    left = []
    right = []
    
    for element in elements[1:]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
         
    return quick_sort(left) + [pivot] + quick_sort(right)
       
from random import randint     
print(quick_sort([randint(1, 100000000) for i in range(70000)]))