def insertion_sort(my_list):
    n = len(my_list)
    for i in range(1,n):
        value = my_list[i]
        j=i
        while j>0 and my_list[j-1] > value:
            my_list[j] = my_list[j-1]
            j = j-1
        my_list[j] = value
    return my_list

test2=[2,7,3,10,34,1,6]
print(test2)
insertion_sort(test2)
print(test2)