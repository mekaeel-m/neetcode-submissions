class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0

        right = len(heights) - 1

        max = 0

        while(left != right):
            localMin = min(heights[left],heights[right])
            if(localMin * (right - left) > max):
                max = localMin * (right - left)
            

            if(localMin == heights[left]):
                left += 1
            else:
                right -= 1

        return max