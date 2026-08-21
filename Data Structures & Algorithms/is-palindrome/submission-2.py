class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for j in range(len(s)):
            if s[j].isalnum() is True:
                t += s[j]
        i = 0
        while i < len(t):
            if t[i].lower() != t[(len(t)-1)-i].lower():
                return False
            i += 1
        return True
        