class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        #Counter counts the frequency of each element within the dataset
        from collections import Counter

        count_s = Counter(s)
        count_t = Counter(t)

        return count_s == count_t
        
