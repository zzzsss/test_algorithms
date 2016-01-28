class Solution(object):
    def twoSum(self,nums,start,end,target,v0,v1,ret):
        end -= 1
        while(start < end):
            v_start = nums[start]
            v_end = nums[end]
            cur_t = v_start + v_end
            if(cur_t == target):
                ret.append([v0,v1,v_start,v_end])
                while(nums[start]==v_start and end>start):
                    start += 1    #whatever
            elif(cur_t < target):
                start += 1    #whatever
            else:
                end -= 1    #whatever
        return
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        if len(nums) < 4:
            return ret
        before_i0 = None
        for i0 in range(0,len(nums)-3):
            #take advantage of sorted
            if target < nums[i0]*4 or target > nums[-1]*4:
                break
            if nums[i0] == before_i0:
                continue
            before_i0 = nums[i0]
            before_i1 = None
            for i1 in range(i0+1,len(nums)-2):
                if nums[i1] == before_i1:
                    continue
                before_i1 = nums[i1]
                new_t = target - nums[i0] - nums[i1];
                self.twoSum(nums,i1+1,len(nums),new_t,nums[i0],nums[i1],ret)
        return ret