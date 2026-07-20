class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumarr=[]
        add=0
        for i in nums:
            add+=i
            sumarr.append(add)
        return sumarr
        