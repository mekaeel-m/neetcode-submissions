class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(char.lower() for char in s if char.isalnum())

        for i in range(len(filtered) // 2 ):
            print(filtered[i], filtered[len(filtered)-1 - i])
            if(filtered[i] != filtered[len(filtered)-1 - i]):
                return False
            
        return True