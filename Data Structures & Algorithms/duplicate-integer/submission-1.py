class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while nums:
            current_num = nums.pop()
            if current_num in nums:
                return True
        
        return False
            
                
            
         