def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
        
    Args:
    ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return "Warning: empty list"
    min_element = max_element = ints[0]
    for element in ints:
        if element < min_element:
            min_element = element
        if element > max_element:
            max_element = element 
    
    return (min_element, max_element) 

## Example Test Case of Ten Integers
import random
##########TEST-1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

###########TEST-2: empty string
print(get_min_max([]))#prints warnning message


######TEST-3: same input
print(get_min_max([1,1,1,1,1,1]))#prints 1
print(get_min_max([0,0,0,0]))#prints 0

########TEST-4: negative values
print(get_min_max([-1,-2, 0, 1]))#prints -2, 1
