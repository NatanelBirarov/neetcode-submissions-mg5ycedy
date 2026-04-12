class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        start = 0
        max_f = 0
        char_freq = defaultdict(int)
        for i in range(len(s)):
            char_freq[s[i]] += 1
            max_f = max(max_f, char_freq[s[i]])

            while (i - start + 1) - max_f > k:
                char_freq[s[start]] -= 1
                start += 1
            longest = max(longest, i - start + 1)
                
        return longest

