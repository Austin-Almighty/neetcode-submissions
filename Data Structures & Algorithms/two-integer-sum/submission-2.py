class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {num: j for j, num in enumerate(nums)}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_map and hash_map[difference] != i:
                return [min(i, hash_map[difference]), max(i, hash_map[difference])]
        