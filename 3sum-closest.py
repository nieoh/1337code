class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums = sorted(nums)
        
        ret = nums[0] + nums[1] + nums[2]
        for i in xrange(0, len(nums)-2):
            new_targ = target - nums[i]
            l = i + 1
            r = len(nums)-1
            cand = nums[l] + nums[r]
            while l < r:
                tmp = nums[l] + nums[r]
                if abs(new_targ - cand) >= abs(new_targ - tmp):
                    cand = tmp
                if nums[l] + nums[r] < new_targ:
                    l += 1
                elif nums[l] + nums[r] > new_targ:
                    r -= 1
                else:
                    break
            pot = nums[i] + cand
            if abs(target-ret) > abs(target-pot):
                ret = pot
        return ret
        
