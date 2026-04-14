class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack[-1]
                if s[i] == ")" and top != "(" or \
                    s[i] == "]" and top != "[" or \
                    s[i] == "}" and top != "{":
                    return False
                stack.pop()
                
        if stack:
            return False

        return True