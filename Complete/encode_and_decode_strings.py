class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""
        for string in strs:
            encodeStr += str(len(string))
            encodeStr += '#'
            encodeStr += string
        
        return encodeStr
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # get length of string
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i=j+1 # skip #

            result.append(s[i:(i+length)])
            i += length
        return result

            
