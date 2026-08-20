class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls=0
        rs=0
        ans=[]
        leftsum=[]
        rightsum=[]
        leftsum.append(ls)
        rightsum.append(rs)
        for i in range(len(nums)-1):
            ls+=nums[i]
            leftsum.append(ls)
        for j in range(len(nums)-1, 0, -1):
            rs+=nums[j]
            rightsum.append(rs)
        rightsum.reverse()
        for k in range(len(nums)):
            ans.append(abs(leftsum[k]-rightsum[k]))
        return ans