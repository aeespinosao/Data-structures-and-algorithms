def insertion_sort(elements):
    for i in range(1, len(elements)):
        temp = elements[i]
        j = i-1
        
        while temp < elements[j] and j >= 0:
            elements[j+1] = elements[j]
            elements[j] = temp
            j-=1
            
    return elements

print(insertion_sort([4,2,6,5,1,3]))