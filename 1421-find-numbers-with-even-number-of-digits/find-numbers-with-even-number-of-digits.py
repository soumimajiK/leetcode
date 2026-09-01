class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            rounds=0
            while i>0:
                i//=10
                rounds+=1
            if rounds%2==0:
                count+=1
        return count
        