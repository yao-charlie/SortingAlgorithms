def quickSort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    pivot_index = 0
    pivot_value = unsorted_list[pivot_index]

    # for compared in range(1, len(unsorted_list)):
    #     if unsorted_list[compared] < pivot_value:
    #         unsorted_list.insert(0, unsorted_list.pop(compared))
    #         pivot_index += 1

    for index, value in enumerate(unsorted_list):
        if value < pivot_value:
            unsorted_list.insert(0, unsorted_list.pop(index))
            pivot_index += 1

    unsorted_list[0:pivot_index] = quickSort(unsorted_list[0:pivot_index])
    unsorted_list[pivot_index + 1:len(unsorted_list)] = quickSort(unsorted_list[pivot_index + 1:len(unsorted_list)])

    return unsorted_list


def mergeSort(unsorted_list):
    # needed for mutating the original list in place by keeping a global variable

    placeholder_list = mergeSortAlgo(unsorted_list)

    # i = 0
    # while i < len(unsorted_list):
    #     unsorted_list[i] = A[i]
    #     i += 1

    # for index, value in enumerate(unsorted_list):
    #     unsorted_list[index] = placeholder_list[index]

    for index in range(len(unsorted_list)):
        unsorted_list[index] = placeholder_list[index]

    return unsorted_list


def mergeSortAlgo(unsorted_list):
    # base case:
    if len(unsorted_list) <= 1:
        return unsorted_list

    # split to base cases recursively

    midpoint = int(len(unsorted_list) / 2)

    left_list = mergeSortAlgo(unsorted_list[0:midpoint])
    right_list = mergeSortAlgo(unsorted_list[midpoint:len(unsorted_list)])

    left_index = 0

    # inserts right into left list by comparing each item

    while left_index < len(left_list) and len(right_list) > 0:
        if right_list[0] <= left_list[left_index]:
            left_list.insert(left_index, right_list.pop(0))

        else:
            left_index += 1

    # if the right list hasn't been emptied because elements are greater, add all to left list:

    if len(right_list) > 0:
        left_list.extend(right_list)

    return left_list
