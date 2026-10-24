class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seendat ={}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seendat:
                return [seendat[diff], i]
            seendat[num] = i




            
        