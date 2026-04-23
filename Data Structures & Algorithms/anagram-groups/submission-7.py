class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagrams(s1, s2):
            if(len(s1) != len(s2)):
                return False
            for i in range(0,len(s1)):
                if s1[i] in s2:
                    s2 = s2.replace(s1[i],"",1)
                else:
                    return False
            return True

        ans = [[strs[0]]]
        added = False
        for x in strs[1:]:
            for y in ans:
                if (x != y and anagrams(x,y[0])):
                    y.append(x)
                    added = True
            if not added: 
                ans.append([x])
            added = False

                        

        return ans

        