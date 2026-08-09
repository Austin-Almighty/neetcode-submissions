class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = max_consec = 0
        for num in nums:
            current_streak = current_streak + 1 if num else 0
            max_consec = max(current_streak, max_consec)
        return max_consec
        