import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def ceil(a: int, b: int):
            #print(num, -round(-num))
            return -(a//-b)
        potions.sort()
        #print(potions)
        needs = [ceil(success, spell) for spell in spells]
        #print(needs)
        result = [len(potions)-bisect.bisect_left(potions, need) for need in needs]
        return result
        