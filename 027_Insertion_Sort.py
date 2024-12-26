def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        
        list[j + 1] = key

test_list = [5,2,6,8,10,3,9,4,12]
insertion_sort(test_list)
print(test_list)
