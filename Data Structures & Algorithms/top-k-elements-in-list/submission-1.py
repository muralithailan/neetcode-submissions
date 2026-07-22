class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= {}

        for i in range(len(nums)):
            if nums[i] in freq:
                counter = freq[nums[i]]
                counter= counter +1
                freq[nums[i]] = counter
            else:
                freq[nums[i]] = 1
        
        sorted_items = sorted(freq.items(), key=lambda item: item[1],reverse=True)
        top_2_keys = [key for key, value in sorted_items[:k]]
        return top_2_keys