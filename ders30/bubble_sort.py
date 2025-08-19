def bubble_sort(lst):
    counter = 0
    for i in range(len(lst)): # range(0,7) -> 0,6
        for j in range(0,len(lst)-1-i): # range()
            if lst[j] > lst[j+1]:
                counter += 1
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

    return lst,counter

print(bubble_sort([2,8,5,3,9,4,1]))
print(bubble_sort([1,2,3,4,5,8,9])) # Best Case Tn = O(n)
print(bubble_sort([9, 8, 5, 4, 3, 2, 1])) # Worst Case Tn = O(n^2)

