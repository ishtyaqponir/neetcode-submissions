class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == None or t == None:
            return False
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        