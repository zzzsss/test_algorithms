class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ans = 0
        i = 0
        minus_flag = False
        #empty string
        while i<len(str) and str[i] == ' ':
        	i += 1
        if i==len(str) or "-+0123456789".find(str[i])==-1:
        	return 0;
        # +- sign
        if str[i]=='+' or str[i]=='-':
        	i += 1
        	if "0123456789".find(str[i])==-1:
        		return 0
        	if str[i-1]=='-':
        		minus_flag = True
        #read them
        while i<len(str) and "0123456789".find(str[i]) != -1:
        	ans = ans*10 + "0123456789".find(str[i])
        	i += 1
        	if(minus_flag and ans >= 2147483648):
        		return -2147483648
        	if(not minus_flag and ans >= 2147483647):
        		return 2147483647
        if minus_flag:
        	ans *= -1
        return ans
