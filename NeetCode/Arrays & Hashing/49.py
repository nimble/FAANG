class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words_arr = []
        for word in strs:
            words_arr.sort()
            if word not in words_arr:
                words_arr.append([word])
            else:
                for words in words_arr:
                    if 

