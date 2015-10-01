class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #set of pointers
        sp = set()
        sp.add(0)
        #forward pointers with possible * --- promise legal *
        i = 0
        while i+1<len(p):
        	if p[i+1]=='*':
        		sp.add(i+2)
        		i += 2
        	else:
        		break
        #main loop --- eat str
        i = 0
        while(True):
        	#end of string
        	if i >= len(s):
        		if len(p) in sp:
        			return True
        		else:
        			return False
        	#eat one piece
        	stmp = set([z+1 for z in sp if z<len(p) and (s[i]==p[z] or p[z]=='.')])
        	#forward with *
        	sp.clear()
        	for z in stmp:
        		if(z<len(p) and p[z]=='*'):
        			sp.add(z-1)
        			sp.add(z+1)
        			ptr = z+1
        			while ptr+1<len(p):
        				if p[ptr+1]=='*':
        					sp.add(ptr+2)
        					ptr += 2
        				else:
        					break
        		else:
        			sp.add(z)
        		#add other *
        		ptr = z
        		while ptr+1<len(p):
        			if p[ptr+1]=='*':
        				sp.add(ptr+2)
        				ptr += 2
        			else:
        				break
        	if not sp:
        		return False
        	i += 1
