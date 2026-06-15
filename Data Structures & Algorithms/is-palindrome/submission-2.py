class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         if len(s) == 0 or not s:
#             return False
#         if len(s) == 1: 
#             return True
#         l, r = 0, len(s) - 1
#         # s = s.strip()
#         while l < r: 
#             if l < r and not s[l].isalnum():
#                 l += 1
#                 continue
#             if r > 1 and not s[r].isalnum():
#                 r -= 1
#                 continue
#             if s[l].lower() != s[r].lower(): 
#                 return False
#             # l += 1
#             # r -= 1
#             l, r = l + 1, r - 1
#         return True


    
        