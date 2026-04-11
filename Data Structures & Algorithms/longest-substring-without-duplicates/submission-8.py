class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupes = {}
        longest = 0
        current = 0
        start = 0
        for i in range(len(s)):
            if s[i] in dupes:
                start = max(dupes[s[i]] + 1, start)
            longest = max(longest, i - start + 1)
            dupes[s[i]] = i

        return longest

