class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum = 0
        for operation in operations:
            if operation[1] == '+':
                sum += 1
            else:
                sum -= 1
        return sum
