class Solution:
    def validPalindrome(self, s: str) -> bool:
        # slices in Python are including first and up to but excluding end
        #[first:end:step]
        if not s: 
            return False
        # if s = s[::-1]: 
        #     return True
        l, r = 0, len(s) - 1
        while l < r: 
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                # if s[l+1] == s[r]:
                #     l += 1
                #     continue
                # if s[r-1] == s[l]:
                #     r -= 1
                #     continue
                skipLeft = s[l+1:r+1]
                skipRight = s[l:r]
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]

        return True

    
    def isAlphaNum(self, c: chr ) -> bool:
        if ord('A') <= ord(c) <= ord('Z') or \
            ord ('a') <= ord(c) <= ord ('z') or \
            ord('0') <= ord(c) <= ord('9'): 
                return True
        return False
        