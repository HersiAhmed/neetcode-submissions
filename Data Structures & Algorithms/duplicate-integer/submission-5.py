class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = []
        for num in nums:
            if num in newList:
                return True
            else:
                newList.append(num)
        return False