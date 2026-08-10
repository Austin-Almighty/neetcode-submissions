class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in index_map:
                return [index_map[dif], i]
            index_map[num] = i