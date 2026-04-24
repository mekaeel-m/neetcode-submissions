class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(char for char in s.lower() if char.isalnum())

        for i in range(len(filtered) // 2 ):
            print(filtered[i], filtered[len(filtered)-1 - i])
            if(filtered[i] != filtered[len(filtered)-1 - i]):
                return False
            
        return True