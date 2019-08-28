def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
        
    Args:
    input_list(list): List to be sorted
    """

    if len(input_list) == 0:
        return "Warning: empty input list"
    zeros_count = ones_count = twos_count = 0

    #traverse the list only ones
    for element in input_list:
        if element == 0:
            zeros_count += 1
        elif element == 1:
            ones_count += 1
        elif element == 2:
            twos_count += 1
        else:
            return -1 #wrong input
    return [0]*zeros_count + [1]*ones_count + [2]*twos_count
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
#######TEST-1
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

#TEST-2: input same type (output should be the same as intput)
print(sort_012([0,0,0,0]))
print(sort_012([1,1,1,1,1,1]))
print(sort_012([2,2,2,2,2]))

########TEST: input contains other than 0, 1 and 2
print(sort_012([1,-2,-5]))#prints -1

##########TEST:4 empty input, prints warning
print(sort_012([]))
