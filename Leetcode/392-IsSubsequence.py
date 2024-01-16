class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        Approach # 2: This time I essentially had two pointers. If the condition was met I'd return true if not false.
        '''

        # Base cases
        if len(s) > len(t):
            return False

        if (len(s) == 0):
            return True
        
        curr = 0
        N = len(t)
        for i in range(N):
            if(s[curr] == t[i]):
                curr+=1
                # Check if we've already met our condition
                if(curr == len(s)):
                    return True
        return False

        '''
        Approach # 1, this did not end up working. But hey, got to think sometimes out of the box lol..
        '''
        # chars1 = list(s)
        # chars2 = list(t)
        # set_chars = set()

        # if(len(chars1) == len(chars2)):
        #     return chars1 == chars2
        # else:
        #     for char in chars2:
        #         if char in chars1:
        #             set_chars.add(char)
            
        #     if(len(set_chars) == len(chars1)):
        #         return chars1 == sorted(list(set_chars))
                    
                    
        #     new_list = sorted(list(set_chars))

        # return sorted(chars1) == new_list
            
