class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        less=-1
        for idx, va in enumerate(nums):
            if va==target:
                return idx
            else:
                if va<target:
                    less=idx
        return less+1
        