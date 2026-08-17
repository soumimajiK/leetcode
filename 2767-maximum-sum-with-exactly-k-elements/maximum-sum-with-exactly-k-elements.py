class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        sadd=nums[-1]
        for _ in range(k-1):
            nums[-1]=nums[-1]+1
            sadd+=nums[-1]
        return sadd