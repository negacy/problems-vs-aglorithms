Dutch National Flag Problem
============================
We are counting number of 0s, 1s, and 2s at a first iteration. Once, the counts are collected, we depend on Python's list operation i.e. [0]*zero counts, [1]*one_counts, and [2]*two_counts. We finally add these three lists and return them.

Time complexity: O(n)

Space complexity: O(m) + O(n) + O(q), where m, n and q are counts of zeros, ones and twos. The total space complexity is linear.
