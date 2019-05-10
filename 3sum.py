class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict = {}
        ret = []
        if not nums:
            return ret
        
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:]):
                if -(a+b) in dict:
                    dict[-a-b].append([i, i+j+1])
                elif a not in dict and b not in dict:
                    dict[-a-b] = [[i, i+j+1]]
                    
        
        for idx, n in enumerate(nums):
            if n in dict:
                for tup in dict[n]:
                    if tup[0] != idx and tup[1]!=idx:
                        ret.append(sorted([nums[tup[0]]]+[nums[tup[1]]]+[n]))
        ret = sorted(ret)
        idx = 0
        nxt = 0
        while idx < len(ret):
            if ret[nxt] != ret[idx]:
                ret[nxt+1], ret[idx] = ret[idx], ret[nxt+1]
                nxt += 1
            idx += 1    
        ret = ret[:nxt+1]
        
        
        
        return ret
