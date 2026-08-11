class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        freq2 = {}
        for i in 'qwertyuiopasdfghjklzxcvbnm':
            freq[i] = 0
            freq2[i] = 0
        for i in s1:
            freq[i] += 1

        left = 0
        

        for right in range(len(s2)):
            freq2[s2[right]] += 1
            if freq2 == freq:
                return True
            else:
                if(right - left + 1 > len(s1)):
                    freq2[s2[left]] -= 1
                    left += 1
                    if freq2 == freq:
                        return True
        return False