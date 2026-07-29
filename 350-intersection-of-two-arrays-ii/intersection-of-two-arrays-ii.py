class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count={}
        uncount={}
        ans=[]
        for i in nums1:
            count[i]=count.get(i, 0)+1
        for j in nums2:
            uncount[j]=uncount.get(j, 0)+1
        matchkeys= list(count.keys() & uncount.keys())
        for k in matchkeys:
            for times in range(min(count[k], uncount[k])):
                ans.append(k)
        return ans