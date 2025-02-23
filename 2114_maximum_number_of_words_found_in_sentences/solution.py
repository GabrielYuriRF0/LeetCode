class Solution:
    @staticmethod
    def countWordsOfSetence(setence: str) -> int:
        return len(setence.split())
    
    def mostWordsFound(self, sentences: list[str]) -> int:
        listCounts = []
        for setence in sentences:
            listCounts.append(self.countWordsOfSetence(setence))
        listCounts.sort()
        return listCounts[-1]