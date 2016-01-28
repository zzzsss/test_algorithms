class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #
        ret = []
        #get counts
        the_map = {}
        for i in nums:
        	if i in the_map:
        		the_map[i] += 1
        	else:
        		the_map[i] = 1
        #n^2 time
        for t1 in the_map.keys():
        	for t2 in the_map.keys():
        		#not enough nums
        		if t1==t2 and the_map[t1]<=1:
        			continue
        		#get from hash
        		t3 = 0-t1-t2
        		need_t3 = [t1,t2].count(t3)+1
        		if t3 not in the_map or the_map[t3] < need_t3:
        			continue
        		#add to set
        		ret.append(sorted([t1,t2,t3]))
        #sort and unique
        ret.sort()
        before = []
        retret = []
        for i in ret:
        	if i==before:
        		continue
        	before = i
        	retret.append(i)
        return retret