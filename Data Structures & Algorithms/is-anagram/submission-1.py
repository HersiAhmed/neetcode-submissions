class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = []
        tList = []
        for letter in s:
            sList.append(letter)
        sList.sort()
        for letter in t:
            tList.append(letter)
        tList.sort()
        return sList == tList