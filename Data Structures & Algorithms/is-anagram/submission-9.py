class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for letter in s:
            count[letter] = count.get(letter, 0) + 1
        for letter in t: 
            count[letter] = count.get(letter, 0) - 1
        
        for value in count.values():
            if(value != 0):
                return False
        return True  