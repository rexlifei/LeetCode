'''
https://leetcode-cn.com/problems/buddy-strings/

思路：
3种情况：
1. 如果长度不等，返回false
2. 如果字符串相同，并且一个字符串里面有重复字符，返回true
3. 找到两个字符串不一样的地方，肯定是有两个点位不一样，并且字符相反


'''

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        if A == B and len(set(A)) < len(A):
            return True
        
        pair = list()
        for i in range(len(A)):
            if A[i] != B[i]:
                pair.append([A[i], B[i]])
        
        if len(pair) != 2:
            return False
        
        if pair[0] != pair[1][::-1]:
            return False
        
        return True
