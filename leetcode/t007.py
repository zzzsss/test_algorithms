import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if x==0:
        	return x
        elif x<0:
        	x = -x
        	flag = True
        tmp = str(x)
        tmp2 = ""
        for i in range(len(tmp)):
        	tmp2 += tmp[len(tmp)-1-i]
        x2 = int(tmp2)
        #overflow
        if not flag and x2 > 2**31 -1:
        	return 0 
        if flag and x2 > 2**31:
        	return 0
        #normal
        if flag:
        	x2 *= -1
        return x2
