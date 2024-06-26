class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_map = {}
        result = []
        # time: O(n)
        for i, s in enumerate(groupSizes):
            if s in size_map:
                size_map[s].append(i)
            else:
                size_map[s] = [i]
            #size_map[s] = size_map[s].append(i) if s in size_map else [i]
            if len(size_map[s]) == s:
                result.append(size_map[s])
                del size_map[s]
        return result