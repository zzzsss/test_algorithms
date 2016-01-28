class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        strlist = ['I','V','X','L','C','D','M'];
        i = 0
        num = 0
        #1.test 1000
        if s[i]=='M':
        	while i<len(s) and s[i]=='M':
        		i += 1
        	num = i*10;
        #2.others
        tmd = 4		#To Match inDex
        while tmd>=0:
        	if i<len(s) and s[i]==strlist[tmd]:
        		if i<len(s)-1 and s[i+1]==strlist[tmd+2]:
        			#9
        			i += 2
        			num += 9
        		elif i<len(s)-1 and s[i+1]==strlist[tmd+1]:
        			#4
        			i += 2
        			num += 4
        		else:
        			#1~3
        			count = 0
        			while i<len(s) and s[i]==strlist[tmd]:
        				i += 1
        				count += 1
        			num += count
        	elif i<len(s) and s[i]==strlist[tmd+1]:
        		num += 5
        		count = 0
        		i += 1
        		while i<len(s) and s[i]==strlist[tmd]:
        			i += 1
        			count += 1
        		num += count
        	num *= 10
        	tmd -= 2
        return num/10