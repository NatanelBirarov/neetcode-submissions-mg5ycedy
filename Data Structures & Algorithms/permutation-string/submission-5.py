class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        perm_s1 = [0] * 26
        perm_s2 = [0] * 26

        for i in range(len(s1)):
            perm_s1[ord(s1[i]) - ord('a')] += 1
            perm_s2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if perm_s1[i] == perm_s2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            perm_s2[index] += 1
            if perm_s1[index] == perm_s2[index]:
                matches += 1
            elif perm_s1[index] + 1 == perm_s2[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            perm_s2[index] -= 1
            if perm_s1[index] == perm_s2[index]:
                matches += 1
            elif perm_s1[index] - 1 == perm_s2[index]:
                matches -= 1           
                
            l += 1

        return matches == 26
