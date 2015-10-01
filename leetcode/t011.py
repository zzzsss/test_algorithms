class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        the_max = 0
        the_all = len(height)
        #left to right
        left_match_height = 0
        right_p = the_all - 1
        left_p = 0
        while right_p > left_p:
        	tmp_r = height[right_p]
        	tmp_l = height[left_p]
        	#1.skip current, there has been match left with higher score
        	if left_match_height >= tmp_l:
        		left_p += 1
        	#2.already right match
        	elif tmp_r >= tmp_l:
        		the_max = max(the_max,tmp_l*(right_p-left_p))
        		left_match_height = tmp_l
        		left_p += 1
        	#3.nope
        	else:
        		right_p -= 1
        #right to left
        right_match_height = 0
        right_p = the_all - 1
        left_p = 0
        while right_p > left_p:
        	tmp_r = height[right_p]
        	tmp_l = height[left_p]
        	#1.skip current, there has been match left with higher score
        	if right_match_height >= tmp_r:
        		right_p -= 1
        	#2.already right match
        	elif tmp_r <= tmp_l:
        		the_max = max(the_max,tmp_r*(right_p-left_p))
        		right_match_height = tmp_r
        		right_p -= 1
        	#3.nope
        	else:
        		left_p += 1
        return the_max
