class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        current_streak = 0
        max_consec = 0
        for num in nums:
            if num == 1:
                current_streak += 1
                max_consec = max(max_consec, current_streak)
            else:
                current_streak = 0
        return max_consec

        