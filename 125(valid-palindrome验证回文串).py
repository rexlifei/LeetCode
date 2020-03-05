'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = [i for i in s.lower() if (i>='a' and i<='z') or (i>='0' and i<='9')]
        return a == a[::-1]
