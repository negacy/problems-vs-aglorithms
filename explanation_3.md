Problem 3: Rearrange Array Digits
===================================
A max heap is used to store elements of the input list. The removal operation is performed to get maximum element in the heap, and for each removeal the elements are appended to the two numbers. These two numbers are retuned, which will give maxim sum.

Time complexity: O(log(n)) since we are using max-heap.

Space complexity: the space complexity is O(n), where n is size of the input list because we are using an array to implement max-heap.
