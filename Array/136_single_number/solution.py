class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        mapeamento = {}
        for i in range(0, len(nums)):
            if(mapeamento.__contains__(nums[i])):
                mapeamento[nums[i]] += 1
            
            else:
                mapeamento[nums[i]] = 0

        resposta = nums[0]
        for k,v in mapeamento.items():
            if v == 0:
                resposta = k
                break
                

        return resposta



solution = Solution()
print(solution.singleNumber([2,2,1]))