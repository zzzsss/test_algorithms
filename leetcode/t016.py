class Solution(object):
    def twoSumClose(self,nums,start,end,t):
        s = start
        e = end
        ret = abs(t-nums[s]-nums[e])
        msum = nums[s]+nums[e]
        while e>s:
            score = nums[s]+nums[e]
            if abs(t-score) < ret:
                ret = abs(t-score)
                msum = score
            if ret == 0:
                return (0,t)
            if score > t:
                e -= 1
            else:
                s += 1
        return (ret,msum)
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        closest = abs(target-(nums[0]+nums[1]+nums[2]))
        msum = (nums[0]+nums[1]+nums[2])
        for i in range(length-2):
            (r,m) = self.twoSumClose(nums,i+1,length-1,target-nums[i])
            if r<closest:
                closest = r
                msum = m+nums[i]
        return msum
