class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
    
        need = Counter(t)
        window = Counter()
        left = 0
        valid = 0 
        res = ""
        
        for right in range(len(s)):
            if s[right] in need:
                window[s[right]] += 1
                if window[s[right]] == need[s[right]]:
                    valid += 1
            
            while valid == len(need):
                if not res or right - left + 1 < len(res):
                    res = s[left:right+1]
                
                if s[left] in need:
                    window[s[left]] -= 1
                    if window[s[left]] < need[s[left]]:
                        valid -= 1
                left += 1
        
        return res