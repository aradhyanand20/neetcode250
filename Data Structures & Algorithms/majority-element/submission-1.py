class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        count = (len(nums)) // 2
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
            
        for k,val in freq.items():
            if val > count:
                return k          
        



            
