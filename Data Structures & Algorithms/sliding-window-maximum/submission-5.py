import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        max_heap = []
        ans = []
        
        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            
            while max_heap and max_heap[0][1] < right - k + 1:
                heapq.heappop(max_heap)
            
            if right >= k - 1:
                ans.append(-max_heap[0][0])
        
        return ans