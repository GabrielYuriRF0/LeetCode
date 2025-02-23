class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = len(s) -1

        if (len(s) % 2 != 0):
            for j in range(0, int (i/2) +1):
                if (i == j):
                    break
                else:
                    aux = s[j]
                    s[j] = s[i]
                    s[i] = aux
                i -= 1
        else:
             for j in range(0, int (i/2) +1):
                if( i - j == 1):
                    aux = s[j]
                    s[j] = s[i]
                    s[i] = aux
                    break
                
                else:
                    aux = s[j]
                    s[j] = s[i]
                    s[i] = aux
                i -= 1