class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counting = {}
        for letter in s:
            counting[letter] = counting.get(letter, 0) + 1
        for letter in t:
            counting[letter] = counting.get(letter, 0) - 1
        for value in counting.values():
            if (value != 0):
                return False
        return True