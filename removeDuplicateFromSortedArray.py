class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #my solution
        if not nums:
            return 0
        
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[j] == nums[i]:
                    nums.pop(j)
                else:
                    j+=1

        return len(nums)

s = Solution()
print(s.removeDuplicates([1,1,2]))