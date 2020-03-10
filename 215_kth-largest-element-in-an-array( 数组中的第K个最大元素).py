'''
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

用类似快排的方法，左右分开。
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 将nums按第k个元素分开，大的放左边，小的放右边
        def partition(ls, pivot_index):
            left, mid, right = [], [], []
            for i in range(len(ls)):
                if ls[i] == ls[pivot_index]:
                    mid.append(ls[i])
                elif ls[i] <ls[pivot_index]:
                    right.append(ls[i])
                else:
                    left.append(ls[i])
            return left, mid, right
        
        def select(ls, k_big):
            pivot_index = random.randint(0, len(ls)-1)
            left, mid, right = partition(ls, pivot_index)
   
            if len(left) >= k_big:
                return select(left, k_big)
            elif len(left) < k_big and len(left + mid) >= k_big:
                return (left + mid)[k_big-1]
            else:
                return select(right, k_big - len(left + mid))
        
        return select(nums, k)
