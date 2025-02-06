
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystackSize = len(haystack)
        needleSize = len(needle)
        words = []

        for i in range(0, (haystackSize - needleSize) +1):
            currentWord = haystack[i]

            tempI = i
            for j in range(1, needleSize):
                tempI = tempI + 1
                currentWord += haystack[tempI]
            
            words.append({'word': currentWord, 'idx':i})
            currentWord = ''
        
        result = [word for word in words if word['word'] == needle]
        return -1 if len(result) == 0 else result[0]['idx']