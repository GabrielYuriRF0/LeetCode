class Solution:
    def romanToInt(self, s: str) -> int:
        mapRomanToInt = {'I': 1, 'V':5, 'X':10,
                         'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        jump = False

        for i in range(0, len(s)):
            if(jump == True):
                jump = False
                continue
            actualChar = s[i]
            if (actualChar == 'I'):
                if(i == len(s) - 1):
                    total += mapRomanToInt[actualChar]
                else:
                    nextChar = s[i + 1]
                    if (nextChar == 'V'):
                        total += 4
                        jump = True
                    elif (nextChar == 'X'):
                        total += 9
                        jump = True
                    else:
                        total += mapRomanToInt[actualChar]
            elif (actualChar == 'X'):
                if(i == len(s) - 1):
                    previousChar = s[i - 1]
                    if(previousChar == 'I'):
                        total += 9
                    else:
                        total += mapRomanToInt[actualChar]
                
                else:
                    nextChar = s[i + 1]
                    if(nextChar == 'L'):
                        total += 40
                        jump = True
                    elif(nextChar == 'C'):
                        total += 90
                        jump = True
                    else:
                        total += mapRomanToInt[actualChar]
            elif (actualChar == 'C'):
                if(i == len(s) - 1):
                    previousChar = s[i - 1]
                    if(previousChar == 'X'):
                        total += 90
                    else:
                        total += mapRomanToInt[actualChar]
                else:
                    nextChar = s[i + 1]
                    if(nextChar == 'D'):
                        total += 400
                        jump = True

                    elif(nextChar == 'M'):
                        total += 900
                        jump = True
                    
                    else:
                        total += mapRomanToInt[actualChar]
            else:
                if(jump == False):
                    total += mapRomanToInt[actualChar]

        return total