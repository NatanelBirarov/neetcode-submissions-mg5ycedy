class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = ""
        m = len(strs)
        
        for s in strs:
            lengths = "," + str(len(s)) + lengths

        lengths += "," + str(m)
        print("".join(strs) + lengths)
        return "".join(strs) + lengths
        

    def decode(self, s: str) -> List[str]:
        strs = []
        str_lengths = []
        len_string = -1
        len_string_s = ""
        num_strings = -1
        num_strings_s = ""
        curr_s = ""

        i = len(s) - 1
        # get num of strings
        while True:
            c = s[i]
            if c == ",":
                num_strings = int(num_strings_s)
                break
            else: 
                num_strings_s = c + num_strings_s
            i -= 1
        print(num_strings)
        if num_strings == 0: return strs
        i -= 1
        # build string lengths array
        while True:
            c = s[i]
            if c == ",":
                len_string = int(len_string_s)
                len_string_s = ""
                str_lengths.append(len_string)

                if len(str_lengths) == num_strings:
                    i -= 1
                    break
            else:
                len_string_s = c + len_string_s
            i -= 1
        print(str_lengths)
        i = 0
        for k in range(len(str_lengths)):
            str_len = str_lengths[k]
            print(str_len)
            print(s[i:i + str_len])
            strs.append(s[i:i + str_len])
            i += str_len
            
        return strs
            




