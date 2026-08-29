class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        # counter_map = [(strings, Counter(sting)) for strings in strs]
        for s in strs:
            count = Counter(s)
            count = dict(count)
            key = tuple(sorted(count.items()))
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        
        return list(res.values())