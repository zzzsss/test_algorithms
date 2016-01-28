class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
        	return ""
        prefix = ""
        minlen = min([len(s) for s in strs])
        for i in range(minlen):
        	cs = set([s[i] for s in strs])
        	if len(cs) > 1:
        		break
        	prefix += cs.pop()
        return prefix