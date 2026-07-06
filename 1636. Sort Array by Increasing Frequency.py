Here the problem statement is 

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3. 

Solution:

1 : 2, 2:3, 3:1 

Now , we need to sort based on the frequencies sorted(nums, lambda x : mpp[x]) 

Prints mpp[x] values: 2, 3, 1

Sorting based on this frequenices, now prints the ans array 3, 1, 1, 2, 2, 2

Now we need to handle edge case with same frequenices, Suppose 2:2 , 3:2 , ans would be 3, 2  

that's why we use tuple pair wise computing , (value, -key) ==> (2, -2), (2, -3) Compare this two pair  -2 < -3 We'll get ans after sorted
based on the numbers 3, 2 ["it's our answer ] 
