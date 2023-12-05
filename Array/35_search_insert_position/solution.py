class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        count = 0
        result = None
        for num in nums:
            if(num == target) or num > target :
               result = count
               break
            count += 1

        return count