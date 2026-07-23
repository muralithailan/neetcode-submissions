class Solution:

    def encode(self, strs: List[str]) -> str:
        str_encode=""
        for i in range(len(strs)):
            str_len=len(strs[i])
            # Using a fixed delimiter like '#' to handle length separation
            encode=f"{str_len}#{strs[i]}"
            str_encode = str_encode+encode

        return str_encode

    def decode(self, s: str) -> List[str]:

        strs =[]
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            word_length = int(s[i:j])
            # Move pointer past the delimiter
            start = j + 1
            # Extract the word based on the length
            decode = s[start : start + word_length]
            strs.append(decode)
            # Move pointer to the start of the next encoded block
            i = start + word_length
        
        return strs
