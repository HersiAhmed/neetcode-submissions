class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = 0
        output = []
        for i, num in enumerate(nums):
          for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                output.append(i)
                output.append(j)
                return output

            
        