class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashSet = {}

        for i in range(len(nums)):

            print(target - nums[i])
            print(hashSet)
            if (target - nums[i] in hashSet.values()):
                return [nums.index(target - nums[i]),i]
            else:
                hashSet[i] = nums[i]
