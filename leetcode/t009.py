class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #assuming neg number can NOT be palindrome
        if x==0:
        	return True
        elif x<0:
        	return False
        #determine how many digits
        i = 0
        tmp = x
        while tmp > 0:
        	tmp /= 10
        	i += 1
        #assuming x must be <= 10 (32bit)
        l = [10**t for t in range(i)]
        #determine the problem in a two-fold
        ##taking care of the first digit
        dl = x%10
        dh = int(x/l[i-1])
        if dl != dh:
        	return False
        ##the rest
        for t in range(1,int(i/2)+1):
        	dl = int(x%(l[t]*10)/l[t])
        	dh = int(x%(l[i-1-t]*10)/l[i-1-t])
        	if dl != dh:
        		return False
        return True