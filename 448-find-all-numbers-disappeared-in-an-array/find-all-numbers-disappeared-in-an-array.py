class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        req=[]
        for i in range(len(nums)):
            index=abs(nums[i])-1
            nums[index]=-abs(nums[index])
        for j in range(len(nums)):
            if nums[j]>0:
                req.append(j+1)
        return req
        