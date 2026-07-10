class Solution:
    def check(self, nums: List[int]) -> bool:
        newnum=0
        if sorted(nums)==nums:
            return True
        else:
            for i in range(len(nums)-1):
                if nums[i+1]<nums[i]:
                    newnum=nums[i+1:]+nums[:i+1]
                if newnum==sorted(nums):
                    return True
        return False
        