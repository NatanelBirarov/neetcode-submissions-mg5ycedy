class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        perm_s1 = [0] * 26
        perm_s2 = [0] * 26
        for char in s1:
            perm_s1[ord(char) - ord('a')] += 1

        l, r = 0, 0
        while r < len(s1) - 1:
            perm_s2[ord(s2[r]) - ord('a')] += 1
            r += 1
            
        while r < len(s2):
            perm_s2[ord(s2[r]) - ord('a')] += 1
            if perm_s1 == perm_s2:
                return True

            perm_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1

        return False
