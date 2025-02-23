class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        score = 0
        maxValue = max(nums)
        for i in range(0, k):
            score += maxValue
            maxValue += 1
        return score
        
solution = Solution
print(solution.maximizeSum(solution,[5,5,5],2))
        