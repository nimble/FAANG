class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        string1 = ""
        string2 = ""
        # Check String 1 "ab#c"
        for v in s:
            if(v != "#"):
                string1+=v
            else:
                # This means we've found a back space, now let's remove the last character in the string
                string1 = string1[:-1] # We're gonna take everything but the last character that was added.
        
        # Check String 2 "ad#c"
        for v2 in t:
            if(v2 != "#"):
                string2+=v2
            else:
                # This means we've found a hashtag, now let's remove the last character in the string
                string2 = string2[:-1] # We're gonna take everything but the last character that was added.
            
        return string1 == string2
