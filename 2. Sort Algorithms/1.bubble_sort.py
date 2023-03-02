def bubble_sort(elements):
    for i in range(len(elements)-1):
        for j in range(len(elements)-i-1):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp

    return elements

print(bubble_sort([4,2,6,5,1,3]))
