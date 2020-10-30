def quickSort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    pivot_index = 0
    pivot_value = unsorted_list[pivot_index]

    for compared in range(1, len(unsorted_list)):
        if unsorted_list[compared] < pivot_value:
            unsorted_list.insert(0, unsorted_list.pop(compared))
            pivot_index += 1

    unsorted_list[0:pivot_index] = quickSort(unsorted_list[0:pivot_index])
    unsorted_list[pivot_index+1:len(unsorted_list)] = quickSort(unsorted_list[pivot_index+1:len(unsorted_list)])

    return unsorted_list