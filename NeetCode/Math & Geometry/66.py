class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_digits = ""
        for d in digits:
            str_digits+=str(d)
        
        int_digit = int(str_digits) + 1

        # convert it back
        new_arr = []
        for digit in str(int_digit):
            new_arr.append(int(digit))
        
        return new_arr