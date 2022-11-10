class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic stack
        stack = [[101, 0]]
        count = []
        temperatures.reverse()
        for i, t in enumerate(temperatures, 1):
            while t >= stack[-1][0]:
                stack.pop()
                
            stack += [[t, i]]
            if len(stack) > 2:
                count += [stack[-1][1] - stack[-2][1]]
            else:
                count += [0]
            #if stack[-2][0] == 101:
            #    count += [0]
            #else:
            #    count += [stack[-1][1] - stack[-2][1]]
        count.reverse()
        return count
                
