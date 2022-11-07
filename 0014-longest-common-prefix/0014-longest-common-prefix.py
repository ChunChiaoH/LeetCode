class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = sorted([(len(s), i) for i, s in enumerate(strs)])
        shortest_len, shortest_index = lens[0]
        shortest_str = strs[shortest_index]
        for i in range(shortest_len):
            if not all([s[i] == shortest_str[i] for s in strs]):
                return shortest_str[:i]
        return shortest_str
        #print(sorted(lens))
        