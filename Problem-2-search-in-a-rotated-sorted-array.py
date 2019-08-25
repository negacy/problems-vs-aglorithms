import sys
idx = -1
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    
    Args:
    input_list(array), number(int): Input array to search and the target
    Returns:
    int: Index or -1
    """
    start_index = 0
    end_index = len(input_list) - 1
    while start_index <= end_index:
        mid_idx = (start_index + end_index)//2 
        left = input_list[:mid_idx]
        right = input_list[mid_idx:]
        try: 
            if input_list[mid_idx] == number:
                return mid_idx
            found = False
            if number >= left[0] and number <= left[-1]:
                start_index = 0
                end_index = mid_idx - 1
                found = True
            else:# number >= right[0]  and number <= right[-1]: 
                start_index = mid_idx + 1

            if not found:
                if  number >= right[0]  and number <= right[-1]: 
                    start_index = mid_idx + 1
                else:
                    end_index = mid_idx + 1
        except IndexError: #if element not found, return -1
            return -1
    return -1 
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

#test empty cases
test_function([[], 10])
