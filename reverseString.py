class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #my solution
        # list modificated in place so new variable is not created
        s[:]= s[::-1]
        
s = Solution()
print(s.reverseString(["h","e","l","l","o"]))