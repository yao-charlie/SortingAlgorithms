def bubble_sort(unsorted_list):
    size = len(unsorted_list)
    for item in range(size):
        for current in range(0, len(unsorted_list)-1-item): #less item sorted with each pass
            if unsorted_list[current] > unsorted_list[current+1]:
                unsorted_list[current], unsorted_list[current+1] = unsorted_list[current+1], unsorted_list[current]



def insertion_sort(unsorted_list):
    for item_index in range(len(unsorted_list)):
        for compare_index in range(0, item_index):
            if unsorted_list[item_index] < unsorted_list[compare_index]:
                unsorted_list.insert(compare_index, unsorted_list.pop(item_index))




def selection_sort(unsorted_list):
    for item in range(len(unsorted_list)):
        min_index = item
        min_value = unsorted_list[min_index]
        for compared_item in range(item, len(unsorted_list)):
            if unsorted_list[compared_item] < min_value:
                min_value = unsorted_list[compared_item]
                min_index = compared_item
        unsorted_list.insert(item, unsorted_list.pop(min_index))



# def cycle_sort(unsorted_list):
#Algo:
#1. Select item 1
#2. count how many items in the list should preceed it (smaller than)
#3. put item into that location while assigning the new item as the new candidate to sort
#4. repeat to 2
#5. How do you conclude the list is completed... visiting every element once?