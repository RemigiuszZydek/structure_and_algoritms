class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        #my solution
        array_from_string = s.split()
        result = ""
        if len(array_from_string) >= k + 1:
            for i in range(len(array_from_string)):
                if i == k:
                    break
                else:
                    result += array_from_string[i]
                    if i < k - 1 :
                        result += " "
        else:
            result = s

        
        return result
    
s = Solution()
print(s.truncateSentence("Ale jajca ja cie krece lol", 4))