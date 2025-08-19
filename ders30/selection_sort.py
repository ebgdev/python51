def selection_sort(lst,n):
    counter = 0
    counter1 = 0
    for current_index in range(n):
        min_index = current_index # min_index = 0 , current_index = 0

        for next_index in range(current_index+1,n): # next_index = 1
            counter1 += 1
            if lst[next_index] < lst[min_index]:
                counter += 1
                min_index = next_index

        lst[min_index] , lst[current_index] = lst[current_index] , lst[min_index]
    
    return lst,counter,counter1


my_list = [2,8,5,3,9,4,1]
print(selection_sort(my_list,len(my_list)))
print(selection_sort([1,2,3,4,5,8,9],len(my_list))) # Best Case Tn = O(n)
print(selection_sort([9, 8, 5, 4, 3, 2, 1],len(my_list))) # Worst Case Tn = O(n^2)
# [1,8,5,3,9,4,2]
# [1,2,5,3,9,4,8]
# [1,2,3,5,9,4,8]
# [1,2,3,4,9,5,8]
# ...