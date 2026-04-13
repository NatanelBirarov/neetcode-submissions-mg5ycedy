class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq_t = {}
        freq_s = {}
        for char in t:
            freq_t[char] = 1 + freq_t.get(char, 0)

        matches = 0
        shortest = len(s) + 1
        l, r = 0, 0
        start = end = -1
        for r in range(len(s)):
            char = s[r]
            freq_s[char] = 1 + freq_s.get(char, 0)
            if char in freq_t and freq_t[char] == freq_s[char]:
                matches += 1

                while matches == len(freq_t):
                    if r - l + 1 < shortest:
                        start, end = l, r
                        shortest = r - l + 1

                    freq_s[s[l]] -= 1
                    if s[l] in freq_t and freq_t[s[l]] - 1 == freq_s[s[l]]:
                        matches -= 1
                    l += 1

        print(start, end, matches, shortest, len(t))
        if shortest == 0:
            return ""

        print(s[start:end + 1])
        return s[start: end + 1]

            

