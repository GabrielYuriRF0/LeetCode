class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        j = 0
        n = len(t)

        for i in range(0, n):
            if count == len(s):
                break
            if t[i] == s[j]:
                j+= 1
                count += 1
        
        if count == len(s):
            return True
        else:
            return False


solution = Solution()
print(solution.isSubsequence("axc", "ahbgdc"))