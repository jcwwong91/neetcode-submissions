class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            encoded_str = f'{chr(len(s))}{s}'
            ret += encoded_str
        return ret

    def decode(self, s: str) -> List[str]:
        ptr = 0
        ret = list()
        while ptr < len(s):
            str_len = ord(s[ptr])
            ostr = s[ptr+1:ptr+str_len+1]
            ret.append(ostr)
            ptr += 1 + str_len
        return ret
