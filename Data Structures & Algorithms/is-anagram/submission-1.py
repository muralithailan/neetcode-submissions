class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}

        for i in range(len(s)):
            counter = 1
            if s[i] in s_dict:
                counter = s_dict[s[i]]
                counter = counter + 1
                s_dict[s[i]] = counter
            else:
                s_dict[s[i]] = counter    
        
        for i in range(len(t)):
            if t[i] not in s_dict:
                return False
            else:
                counter = s_dict[t[i]]
                if counter > 0:
                    counter = counter -1
                
                if counter == 0:

                    s_dict.pop(t[i])
                else:
                    s_dict[t[i]] =counter
                

        if len(s_dict) > 0:
            return False
        
        return True
        