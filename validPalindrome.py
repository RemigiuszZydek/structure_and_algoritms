import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #my solution

        new_word = re.sub("[^a-zA-Z0-9]","",s)
        reversed_new_word = "".join(reversed(new_word))
        if new_word.lower() == reversed_new_word.lower():
            return True
        else:
            return False
        
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))