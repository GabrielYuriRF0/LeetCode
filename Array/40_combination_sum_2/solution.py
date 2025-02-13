class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutions = []
        def calculateSum(candidates, target, currentSum, currentSolution, i, n):
            if currentSum == target:
                solutions.append(currentSolution[:])
            elif i < n :
                currentSolution[i] = candidates[i]
                calculateSum(candidates, target, currentSum + candidates[i], currentSolution[:], i +1,n)
                
        
        n = len(candidates)
        currentSolution = [None] * n

        calculateSum(candidates, target, 0, currentSolution, 0, n)
        return solutions


solution = Solution()
print(solution.combinationSum2([1, 2, 5, 6, 8], 9))



