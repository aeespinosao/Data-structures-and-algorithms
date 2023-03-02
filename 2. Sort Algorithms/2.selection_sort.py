def selection_sort(elements):
    for i in range(len(elements)):
        min_index = i
        for j in range(i+1, len(elements)):
            if elements[min_index] > elements[j]:
                min_index = j
        if i != min_index:
            temp = elements[i]
            elements[i] = elements[min_index]
            elements[min_index] = temp

    return elements
    

print(selection_sort([4,2,6,5,1,3]))
