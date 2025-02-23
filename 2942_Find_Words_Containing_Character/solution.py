class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indexs = []
        index = 0
        for word in words:
            if x in word:
                indexs.append(index)

            index += 1
        
        return indexs

        