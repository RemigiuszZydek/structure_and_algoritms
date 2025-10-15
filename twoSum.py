from typing import List
class Solution(object):
    # my solution
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        result = []

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)

        return result
    
    # neetcode solution
    
    def twoSumTwo(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target -n
            if diff in prevMap:
                return[prevMap[diff],i]
            prevMap[n] = i
        return 

    
s = Solution()
print(s.twoSumTwo([2,7,11,15],9))


