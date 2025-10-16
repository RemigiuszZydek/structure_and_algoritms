class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
        #my solution
        if ch in word:
            new_word = list(word)
            ch_index = word.index(ch)
            number_of_for = ch_index 
            for i in range(ch_index + 1) :
                new_word[i] = word[number_of_for]
                number_of_for -= 1
            
            return ''.join(new_word)
        return word
            
s = Solution()
print(s.reversePrefix('zxczxasdsa',"d"))