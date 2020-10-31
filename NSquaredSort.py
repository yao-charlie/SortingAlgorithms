def bubbleSort(unsorted_list):
    size = len(unsorted_list)
    for item in range(size):
        for current in range(0, len(unsorted_list) - 1 - item):  # less item sorted with each pass
            if unsorted_list[current] > unsorted_list[current + 1]:
                unsorted_list[current], unsorted_list[current + 1] = unsorted_list[current + 1], unsorted_list[current]
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


def pseudoCycleSort(unsorted_list):
    # My implementation trades off one count on each item by using a dictionary to keep track of cycles visited.
    # Memory complexity ~= 2n (changed dict to set). Using dict could be useful to index # of duplicate items:
    # {index: [value, #]}
    # Edit: writes can still be minimized but more 'faster memory' is required. Better for flash, worse for EEPROM.
    # Time complexity = O(n^2) still but maybe O(n^2/k) where k is the number of loops? Seems reasonable - n^2 if k = 1
    # n if k = n loops, meaning all items are in the right place already.

    # need check for empty list due to list index to start logic.
    if not unsorted_list:
        return unsorted_list

    # initialize values
    item_index = 0
    sorted_indexes = set()
    item_value = unsorted_list[item_index]
    list_size = len(unsorted_list)
    loop_root = item_index

    # Repeat the enclosed for n elements in the list
    for total_items in range(list_size):

        # counter tally for elements that are smaller
        greater_than_index = 0

        # count how many items in the list should precede it (smaller than)
        for compare_item in range(len(unsorted_list)):
            # skip the 1st moved element in a loop.
            if compare_item == loop_root:
                continue

            if unsorted_list[compare_item] < item_value:
                greater_than_index += 1

        # track current index to determine if it's already in 'a' right place, if not the beginning of the right
        # place (duplicate entries)
        current_index = item_index
        item_index = greater_than_index
        # Find the index to insert into to sort based on the following:
        # if the items are the same, find the next empty location to insert
        # if you reach the same position, it's already sorted so exit loop
        # if you reach the end of the list, it will be inserted at the end of the list.
        while (item_value == unsorted_list[item_index]) and (item_index != current_index) and (item_index < list_size):
            item_index += 1

        # Swap values
        item_value, unsorted_list[item_index] = unsorted_list[item_index], item_value

        # Q: need to prevent loops so need to keep track of sorted items - but does that increase writes, negating cycle
        # advantage? Necessary evil?
        # A: apparently not - just brute force each item to see if it's in the right place every time you visit it.

        sorted_indexes.add(item_index)

        # check if we've completed a loop
        if item_index == loop_root:
            # check if we've sorted everything. Could just return instead?
            if len(sorted_indexes) == list_size:
                break
            # advance through list until you find a loop you've not traversed
            item_index += 1
            while item_index in sorted_indexes:
                item_index = (item_index + 1) % list_size

            # discard final value from previous loop by picking up the newly discovered value
            item_value = unsorted_list[item_index]
            # re-assign to new root value.
            loop_root = item_index

    return unsorted_list
