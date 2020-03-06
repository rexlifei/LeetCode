'''
https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/submissions/

反转字符串中的每个单词

一行代码搞定：
return ' '.join(i[::-1] for i in s.split())

'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        split_s = s.split(' ')

        new_s = list()
        for i in split_s:
            new_s.append(i[::-1])

        return ' '.join(new_s)
