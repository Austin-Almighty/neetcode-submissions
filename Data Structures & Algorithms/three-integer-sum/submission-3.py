class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue
            target = -num
            l, r = idx + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        
        return res