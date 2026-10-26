class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a notebook to store the positions
        collected = {}
        # loop through the list and giving access to the position and the number itself
        for i, num in enumerate(nums):
            # find the differences by subtracting the current number from the target
            diff = target - num
            # if the diff is in the collected dict
            if(diff in collected):
                # return the the position of the diff along with the index of the current number we are looking at
                return [collected[diff], i]
            # if the diff isn't in the notebook, then store the current numbers position into the notebook
            collected[num] = i
        
