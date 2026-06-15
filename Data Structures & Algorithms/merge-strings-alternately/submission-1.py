class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 or not word2:
            return ""
        return_str = ""
        len1 = len(word1)
        len2 = len(word2)
        minLen = min(len1, len2)

        for i in range(minLen):
            return_str += word1[i]
            return_str += word2[i]
        
        if len1 > minLen:
            return_str += word1[minLen:len1]
        if len2 > minLen:
            return_str += word2[minLen:len2]
        return return_str
