class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupes = {}
        longest = 0
        current = 0
        start = 0
        for i in range(len(s)):
            if s[i] in dupes and dupes[s[i]] >= start:
                start = dupes[s[i]] + 1
                current = i - start + 1
            else:
                current += 1
            longest = max(longest, current)
            dupes[s[i]] = i
            print(longest, current, start, dupes)

        return longest

