'''
https://leetcode-cn.com/problems/valid-palindrome/
思路：先把数字和字母提取出来，然后反转，判断是否和原字符串一致。

改进：可以尝试只对比前半段和后半段的反转，判断是否一致。
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = [i for i in s.lower() if (i>='a' and i<='z') or (i>='0' and i<='9')]
        return a == a[::-1]
