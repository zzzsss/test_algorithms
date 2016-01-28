class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        strlist = ['I','V','X','L','C','D','M'];
        ret = "";
        count = 0;
        while num > 0:
        	d = num % 10;
        	num = num / 10;
        	cur = ""
        	if d <= 3:
        		for i in range(d):
        			cur += strlist[2*count];
        	elif d == 4:
        		cur = strlist[2*count] + strlist[2*count+1];
        	elif d <= 8:
        		cur = strlist[2*count+1]
        		for i in range(d-5):
        			cur += strlist[2*count];
        	else:
        		cur = strlist[2*count] + strlist[2*count+2];
        	ret = cur + ret
        	count += 1
        return ret