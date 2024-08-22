class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort the arrays
        strs.sort()
        i = 0
        lcf = ""

        for i in range(len(strs[-1])):
            if(strs[0][i] == strs[-1][i]):
                lcf+=strs[0][i]
            else:
                return lcf
        return lcf
