class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        snums = sorted(nums)
        n1 = 0
        for i,j in enumerate(snums):
            try:
                snums.index(target-j,i+1)
                n1 = j
                break
            except:
                pass
        #original list
        n2 = target - n1
        ret = []
        for i,j in enumerate(nums):
            if j==n2:
                ret.append(i+1)
            elif j==n1:
                ret.append(i+1)
            if len(ret) == 2:
                break
        return ret

x = Solution()
print(x.twoSum([3,2,4],6))
