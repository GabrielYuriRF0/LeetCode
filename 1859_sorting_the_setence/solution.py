class Solution:
    def sortSentence(self, s: str) -> str:
        dictPalavras = {1:'', 2:'', 3:'', 4:'',
                    5:'', 6:'', 7:'', 8:'', 9:''}
        palavasSoltas = s.split()
        resultado = ''
        
        for palavra in palavasSoltas:
            dictPalavras[int(palavra[-1])] = palavra[:len(palavra) - 1]

        for value in dictPalavras.values():
            if (value != ''):
                resultado += value + ' '

        return resultado[:len(resultado) - 1]