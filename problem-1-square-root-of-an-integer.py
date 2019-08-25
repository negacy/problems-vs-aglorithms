def sqrt(number):
    """
        Calculate the floored square root of a number
        
        Args:
        number(int): Number to find the floored squared root
        Returns:
        int: Floored Square Root
        """
    if number == 0:
        return 0
    if number < 0 :
        print("Warnning: input is negative")
        return -1
    if type(number) != int:
        print("Warnning: input should be an integer")
        return -1
    #using Newthon's method
    x = number
    y = (number + 1)//2

    while y < x:
        x = y
        y = (x + number//x)//2
    return x 

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

###negative cases
print ("Pass" if  (-1 == sqrt(-1)) else "Fail")

##floating numbers
print ("Pass" if  (-1 == sqrt(1.123)) else "Fail")

##
print ("Pass" if  (1 == sqrt(2)) else "Fail")
