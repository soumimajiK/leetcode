class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        index=len(nums)-k
        nums[:]=nums[index:]+nums[:index]
        return nums
        