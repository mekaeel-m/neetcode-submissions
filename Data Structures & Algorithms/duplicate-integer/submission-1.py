class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numHash = {}
        for i in range(len(nums)):
            if(not nums[i] in numHash):
                numHash[nums[i]] = True
            elif (numHash[nums[i]] == True):
                return True
            
            
        return False