class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_idx, nums2_idx = m-1, n-1
        for i in range(m+n-1, -1, -1):
            if nums2_idx < 0:
                break
            if nums1_idx < 0:
                nums1[i] = nums2[nums2_idx]
                nums2_idx -= 1
            # elif nums2_idx < 0:
            #     nums1[i] = nums1[nums1_idx]
            #     nums1_idx -= 1
            elif nums1[nums1_idx] >= nums2[nums2_idx]:
                nums1[i] = nums1[nums1_idx]
                nums1_idx -= 1
            else:
                nums1[i] = nums2[nums2_idx]
                nums2_idx -= 1