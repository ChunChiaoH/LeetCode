import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def ceil(a: int, b: int):
            return -(a//-b)
        potions.sort()
        needs = [ceil(success, spell) for spell in spells]
        result=[]
        cache={}
        for need in needs:
            if need not in cache:
                cache[need]=len(potions)-bisect.bisect_left(potions, need)
            result.append(cache[need])
        return result
        