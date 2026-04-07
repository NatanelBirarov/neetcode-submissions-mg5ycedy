class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        err = 0
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return self.validPal(s, l + 1, r) or self.validPal(s, l, r - 1)
            l, r = l + 1, r - 1
        return True

    def validPal(self, s: str, l: int, r: int):
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True




        # def validPal(s: str, l: int, r: int, err: int):
        #     if l > r:
        #         return True
        #     while l < r and not s[l].isalnum():
        #         l += 1
        #     while r > l and not s[r].isalnum():
        #         r -= 1 
        #     if s[l].lower() != s[r].lower():
        #         err += 1
        #         if err == 2:
        #             return False
        #         return validPal(s, l + 1, r, err) or validPal(s, l, r - 1, err)
        #     return validPal(s, l + 1, r - 1, err)
        # return validPal(s, 0, len(s) - 1, 0)