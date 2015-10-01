class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0:
        	return ""
        if numRows == 1:
        	return s
        strings = ["" for i in range(numRows)]
        count = 0
        plus = True
        for c in s:
        	strings[count] += c
        	if plus:
        		count += 1
        		if count >= numRows:
        			plus = False
        			count -= 2
        	else:
        		count -= 1
        		if count < 0:
        			plus = True
        			count += 2
        	
        ret = ""
        for i in strings:
        	ret += i
        return ret
