class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximus=max(nums)
        for i in range(len(nums)):
            if nums[i]!=maximus:
                if maximus>=nums[i]*2:
                    continue
                else:
                    return -1
            else:
                idx=i
        return idx