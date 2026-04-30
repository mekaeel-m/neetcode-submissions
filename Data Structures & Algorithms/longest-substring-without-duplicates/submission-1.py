class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        found = set()
        left = 0

        for right in range(len(s)):

            while(s[right] in found):
                found.remove(s[left])
                left += 1
            
            found.add(s[right])
            ans = max(ans, right - left + 1)
            
        return ans