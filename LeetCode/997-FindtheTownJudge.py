class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Array for people pointing to other people
        in_degree = defaultdict(int)
        # Array for incoming points.
        out_degree = defaultdict(int)
        
        # Calculate the amount of in-degrees and out-degrees
        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1
        
        # If the Judge isn't pointing to anyone and everyone but himself is pointing to him, that's our JUDGE. Else, we'll return -1.
        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i
        
        return -1
