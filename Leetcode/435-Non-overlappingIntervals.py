class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort the intervals based on the second value of the arrays.
        intervals = sorted(intervals, key = lambda x:x[1])
        ITR = 0
        starting_interval = float('-inf')
        for interval in intervals:
            if(interval[0] >= starting_interval):
                starting_interval = interval[1]
            else:
                ITR+=1
        return ITR
