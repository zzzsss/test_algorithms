class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #scan once (but also o(n) lookback) is okay
        maxlen = 0		#longest length
        curbegin = 0	#current length begin
        cmap = {}		#map char to index
        for i in range(len(s)):
        	ind = cmap.get(s[i])
        	if ind != None and ind>=curbegin:
        		maxlen = max(maxlen,i-curbegin)     
        		curbegin = ind + 1
        	cmap[s[i]] = i
        #the last one
        maxlen = max(maxlen,len(s)-curbegin)
        return maxlen

x=Solution()
x.lengthOfLongestSubstring("abba")