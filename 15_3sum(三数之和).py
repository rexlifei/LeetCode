‘’‘
三数之和
https://leetcode-cn.com/problems/3sum/

主要难度在于结果不能重复，提交不能超时, 不然的话会简单很多。
先排序，然后用双指针解决
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        res = list()
        
        for i in range(len(nums) - 2):
            # 如果第一个数字就大于0
            if nums[i] > 0:
                break
            # 避免重复结果
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 定义两个指针
            left, right = i+1, len(nums) - 1

            while left < right and nums[i] + nums[left] <= 0:
                # 下面两个if 避免重复数字
                if left > i + 1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if right < len(nums) - 1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                
                tri_sum = nums[i] + nums[left] + nums[right]

                if tri_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif tri_sum < 0:
                    left += 1
                else:
                    right -= 1

        return res
