class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        m = len(strs)
        
        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded
        

    def decode(self, s: str) -> List[str]:
        strs = []
        len_string = -1
        len_string_s = ""

        i = 0
        while i < len(s):
            while s[i] != "#":
                len_string_s += s[i]
                i += 1
            len_string = int(len_string_s)
            i += 1
            strs.append(s[i:i + len_string])
            i += len_string
            len_string_s = ""
            
        return strs
            




