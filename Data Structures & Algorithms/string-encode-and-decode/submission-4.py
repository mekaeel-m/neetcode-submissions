class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for x in strs: ans = ans + (str(len(x)) + "#" + x)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while(i < len(s) - 1):
            second = i
            while(second <= len(s) and s[second] != "#"):
                second += 1
            itemLen = int(s[i:second])
            ans.append(s[i + 1 + len(str(itemLen)):i+1 +itemLen + len(str(itemLen))])
            i = i + itemLen + 1 + len(str(itemLen))
        return ans