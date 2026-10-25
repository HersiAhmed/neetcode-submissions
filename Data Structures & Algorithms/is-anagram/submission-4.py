class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = []
        tList = []
        if len(s) != len(t):
            return False
        for letter in s:
            sList.append(letter)
        for letter in t:
            tList.append(letter)
        sList.sort()
        tList.sort()
        if(sList == tList):
            return True
        return False