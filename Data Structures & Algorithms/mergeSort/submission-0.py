# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) < 2:
            return pairs
        mid = len(pairs)//2

        left = pairs[:mid]
        right = pairs[mid:]

        sorted_left = self.mergeSort(left)
        sorted_right = self.mergeSort(right)

        return self.merge(sorted_left, sorted_right)

    def merge(self, first: List[Pair], second: List[Pair]) -> List[Pair]:
        x = y = 0
        res = []
        while x < len(first) and y < len(second):
            if first[x].key <= second[y].key:
                res.append(first[x])
                x += 1
            else:
                res.append(second[y])
                y += 1
        while x < len(first):
            res.append(first[x])
            x += 1
        while y < len(second):
            res.append(second[y])
            y += 1
        return res