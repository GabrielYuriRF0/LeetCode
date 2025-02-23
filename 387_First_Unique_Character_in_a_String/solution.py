class Solution:
    def firstUniqChar(self, s: str) -> int:
        wordMap = {}
        cont = 0
        result = -1
        for char in s:
            if (wordMap.keys().__contains__(char) == False):
                wordMap[char] = [0, cont]
            wordMap[char][0] +=1
            cont += 1
        
        for value in wordMap.values():
          if(value[0] == 1):
              result = value[1]
              break
        return result