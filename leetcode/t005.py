class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
		#return the interval [i,j)
		#0.maximum len
        if len(s) <= 1:
        	return s
        maxlen = 1
        max_s = -1
        max_e = -1
        #1.len(s) is odd
        for i in range(len(s)):
        	maxd = min(i,len(s)-i-1)
        	f_break = False			#early break flag
        	for d in range(maxd+1):
        		if s[i-d] != s[i+d]:
        			#update the new maxlen
        			if 2*d-1 > maxlen:
        				maxlen = 2*d-1
        				max_s = i-d+1
        				max_e = i+d-1
        			f_break = True
        			break
        	if (not f_break) and 2*maxd+1 > maxlen:
        		maxlen = 2*maxd+1
        		max_s = i-maxd
        		max_e = i+maxd
        #2.len(s) is even
        for i in range(len(s)-1):
        	maxd = min(i,len(s)-i-2)
        	f_break = False
        	for d in range(maxd+1):
        		if s[i-d] != s[i+1+d]:
        			#update the new maxlen
        			if 2*d > maxlen:
        				maxlen = 2*d
        				max_s = i-d+1
        				max_e = i+d
        			f_break = True
        			break
        	if (not f_break) and 2*maxd+2 > maxlen:
        		maxlen = 2*maxd+2
        		max_s = i-maxd
        		max_e = i+maxd+1
        #3.return
        return s[max_s:max_e+1]

