class Solution:
    def isHappy(self, n: int) -> bool:        
        cur = n
        visited = set()
        while True:
            cur = sum([int(d)**2 for d in str(cur)])
            if cur == 1: return True
            if cur in visited: return False
            visited.add(cur)