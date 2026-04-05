class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sSort = "".join(sorted(s))
        tSort = "".join(sorted(t))
        for i in range(len(s)):
            if sSort[i] != tSort[i]:
                return False
        return True