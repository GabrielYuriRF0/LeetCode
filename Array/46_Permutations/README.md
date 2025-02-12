# 46. Permutations
Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order.

## Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

## Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

## Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

## Example 3:
    Input: nums = [1]
    Output: [[1]]


## Constraints:
- 1 <= nums.length <= 6
- 10 <= nums[i] <= 10
- All the integers of nums are unique.