class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        ansSet = set()
        for i in range(1, len(nums)):

            left = 0
            right = len(nums) - 1

            while(i != right and i != left):
                if(nums[left] + nums[i] + nums[right] < 0):
                    left += 1
                elif (nums[left] + nums[i] + nums[right] > 0):
                    right -= 1
                else:
                    print("found")
                    ansSet.add((nums[left],nums[i],nums[right]))
                    left += 1
                    
                    
        
        return list(ansSet)


