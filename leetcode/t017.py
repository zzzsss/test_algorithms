class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = [" ","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        list_before = [""]
        for i in digits:
        	n = "0123456789".index(i)
        	if n==1:
        		continue
        	list_tmp = []
        	for s in list_before:
        		for let in nums[n]:
        			list_tmp.append(s+let)
        	list_before = list_tmp
        list_before = [t for t in list_before if len(t)>0]
        return list_before