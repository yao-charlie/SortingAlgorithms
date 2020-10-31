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
    unsorted_list[pivot_index + 1:len(unsorted_list)] = quickSort(unsorted_list[pivot_index + 1:len(unsorted_list)])

    return unsorted_list


def mergeSort(unsorted_list):
    # base case:
    if len(unsorted_list) <= 1:
        return unsorted_list

    # split to base cases

    left_list = mergeSort(unsorted_list[0: int(len(unsorted_list) / 2)])
    right_list = mergeSort(unsorted_list[int(len(unsorted_list) / 2): len(unsorted_list)])

    left_index = 0

    # inserts right into left list

    while left_index < len(left_list) or len(right_list) != 0:
        if len(right_list) == 0:
            break

    # while left_index < len(left_list) or right_list != None:
    #
    #
    #     if right_list is None:
    #         break

        elif len(unsorted_list) <= 1:
            break

        elif left_index == len(left_list):
            left_list.append(right_list[0])
            break

        elif left_list[left_index] > right_list[0]:

            left_list.insert(left_index, right_list.pop(0))
            left_index += 1

        elif left_list[left_index] < right_list[0]:
            left_index += 1

        else:
            left_list.append(right_list.pop(0))

    if len(left_list) == len(unsorted_list):
        unsorted_list = left_list
        return unsorted_list

    # may not be needed - first conditional might return before this ever happens?
    return left_list