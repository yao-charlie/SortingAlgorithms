def bubbleSort(unsorted_list):
    size = len(unsorted_list)
    for item in range(size):
        for current in range(0, len(unsorted_list)-1-item): #less item sorted with each pass
            if unsorted_list[current] > unsorted_list[current+1]:
                unsorted_list[current], unsorted_list[current+1] = unsorted_list[current+1], unsorted_list[current]
    return unsorted_list


def insertionSort(unsorted_list):
    for item_index in range(len(unsorted_list)):
        for compare_index in range(0, item_index):
            if unsorted_list[item_index] < unsorted_list[compare_index]:
                unsorted_list.insert(compare_index, unsorted_list.pop(item_index))
    return unsorted_list




def selectionSort(unsorted_list):
    for item in range(len(unsorted_list)):
        min_index = item
        min_value = unsorted_list[min_index]
        for compared_item in range(item, len(unsorted_list)):
            if unsorted_list[compared_item] < min_value:
                min_value = unsorted_list[compared_item]
                min_index = compared_item
        unsorted_list.insert(item, unsorted_list.pop(min_index))
    return unsorted_list

def cycle_sort_dep(unsorted_list):
    # 1. Select item 1, initialize value
    item_index = 0
    sorted_indexes = {}
    item_value = unsorted_list[item_index]
    loop_root = item_value #needed to not double-count in comparison
    list_size = len(unsorted_list)
    last_element = list_size - 1


    # 5. How do you conclude the list is completed... visiting every element once?
    for total_items in range(list_size+2):
    # 4. repeat to 2, reset count

        greater_than_index = 0


        for compare_item in unsorted_list:
            # 2. count how many items in the list should precede it (smaller than)
            if compare_item < item_value:
                greater_than_index += 1

        if item_value > loop_root:
            greater_than_index -= 1

        # 3. put item into that location while assigning the new item as the new candidate to sort

        unsorted_list.insert(greater_than_index, item_value)

        last_item_index = item_index


        item_index = greater_than_index + 1

        while (item_value == unsorted_list[item_index]) and (item_index < list_size): #if the items are the same, find the next empty location to insert.
            item_index +=1
        item_value = unsorted_list.pop(item_index)

        item_index -= 1

        if last_item_index == greater_than_index:
            item_index = (item_index+1) % list_size
            item_value = unsorted_list[item_index]
            loop_root = item_value

        #need to prevent loops so need to keep track of sorted items - but does that increase writes, negating cycle advantage?
        # item_index_temp = item_index
        if item_index in sorted_indexes:
            while item_index in sorted_indexes:
                item_index = (item_index+1) % list_size

            item_value = unsorted_list[item_index]
            loop_root = item_value
            #N.B could keep a variable to stop updating it every check. Doesn't improve asymptotic complexity but could improve writes


        sorted_indexes[greater_than_index] = greater_than_index



def cycleSort(unsorted_list):
    item_index = 0
    sorted_indexes = {}
    item_value = unsorted_list[item_index]
    list_size = len(unsorted_list)
    loop_root = item_index


    # 5. How do you conclude the list is completed... visiting every element once?
    for total_items in range(list_size):
    # 4. repeat to 2, reset count

        greater_than_index = 0

    # 2. count how many items in the list should precede it (smaller than)
        for compare_item in range(len(unsorted_list)):
            #skip the 1st moved element in a loop.
            if compare_item == loop_root:
                continue

            if unsorted_list[compare_item] < item_value:
                greater_than_index += 1

        item_index = greater_than_index
        # 3. put item into that location while assigning the new item as the new candidate to sort

        # if the items are the same, find the next empty location to insert:
        # while (item_value == unsorted_list[item_index]) and (item_index < list_size):
        while item_value == unsorted_list[item_index]:
            item_index += 1

        item_value, unsorted_list[item_index] = unsorted_list[item_index], item_value

    # need to prevent loops so need to keep track of sorted items - but does that increase writes, negating cycle advantage?
        sorted_indexes[greater_than_index] = greater_than_index
        if item_index == loop_root:
            while item_index in sorted_indexes:
                item_index = (item_index + 1) % list_size
                if len(sorted_indexes) == list_size:
                    break

            item_value = unsorted_list[item_index]
            loop_root = item_index

        # sorted_indexes[greater_than_index] = greater_than_index

    return unsorted_list