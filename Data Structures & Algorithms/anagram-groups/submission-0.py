class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_strs ={}

        for i in range(len(strs)):
            sort_str = "".join(sorted(strs[i]))
            if sort_str in map_strs:
                arr_strs = map_strs[sort_str]
                arr_strs.append(strs[i])
                map_strs[sort_str] = arr_strs
            else:
                map_strs[sort_str] = [strs[i]]
        
        return list(map_strs.values())
