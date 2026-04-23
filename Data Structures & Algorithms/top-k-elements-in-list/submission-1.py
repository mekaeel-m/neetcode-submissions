class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        ans = []

        freq_values = list(freq.values())
        freq_keys = list(freq.keys())

        for i in range(k):
            ans.append(freq_keys[freq_values.index(max(freq_values))])
            freq.pop(freq_keys[freq_values.index(max(freq_values))])
            freq_values = list(freq.values())
            freq_keys = list(freq.keys())

        return ans
    