class Solution:
    def permute(self, nums):
        permutations = []

        def generatePermutations(nums, currentSolution, n ,i):
            if None not in currentSolution[:] and i == n:
                permutations.append(currentSolution[:])

            else:
                for j in range(0,n):
                    if nums[j] not in currentSolution:
                        currentSolution[i] = nums[j]
                        generatePermutations(nums,currentSolution[:], n, i+1)


        n = len(nums)
        i = 0
        currentSolution = [None] * n

        generatePermutations(nums, currentSolution,n,i)
        return permutations
