class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_s = ""
        i = 0
        while i < len(word1) and i < len(word2):
            new_s += word1[i]
            new_s += word2[i]
            i += 1
        while i < len(word1):
            new_s += word1[i]
            i += 1
        while i < len(word2):
            new_s += word2[i]
            i += 1
        return new_s   