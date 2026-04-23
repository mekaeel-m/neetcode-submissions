class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(nums == []):
            return 0
        longest = []
        for i in nums:
            if not (i in longest):
                longest.append(i)
        longest.sort()
        count = 1
        temp = 1
        for i in range(1,len(longest)):
            if (longest[i - 1] == longest[i] - 1):
                temp += 1
            else:
                if temp > count:
                    count = temp
                temp = 1

        return max(count,temp)
        

        