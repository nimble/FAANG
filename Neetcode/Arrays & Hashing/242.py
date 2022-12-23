class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_str = sorted(s)
        second_str = sorted(t)
        if(first_str == second_str):
            return True
        else:
            return False