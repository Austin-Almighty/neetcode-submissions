class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_list = [0] * (2*len(nums))
        for i, num in enumerate(nums):
            new_list[i] = num
            new_list[i+n] = num
        return new_list