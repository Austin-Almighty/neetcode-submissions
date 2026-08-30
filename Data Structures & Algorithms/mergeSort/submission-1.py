# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:
        if (end - start + 1) <= 1:
            return pairs
        
        mid = (start + end) // 2

        self.mergeSortHelper(pairs, start, mid)
        self.mergeSortHelper(pairs, mid+1, end)

        self.merge(pairs, start, mid, end)

        return pairs

    def merge(self, pairs: List[Pair], start, middle, end) -> None:
        L = pairs[start: middle + 1]
        R = pairs[middle + 1: end + 1]

        l, r, i = 0, 0, start

        while l < len(L) and r < len(R):
            if L[l].key <= R[r].key:
                pairs[i] = L[l]
                l += 1
            else:
                pairs[i] = R[r]
                r += 1
            i += 1
        
        while l < len(L):
            pairs[i] = L[l]
            l += 1
            i += 1
        while r < len(R):
            pairs[i] = R[r]
            r += 1
            i += 1