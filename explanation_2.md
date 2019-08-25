Problem 2: Search in a Rotated Sorted Array
==============================================

A binary search apporach is used to find the index of a tart number in a rotated sorted array. We split the given array into two left and right havles. The assumption is that one of these halves should be sorted. First, we search the target number within the sorted array. If the target number is not within the sorted array, then we search it on the unsorted array.

Time complexity: log(n)

Space complexity: O(1)
