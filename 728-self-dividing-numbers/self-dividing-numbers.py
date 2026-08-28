class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left, right+1):
            num=[int(d) for d in str(i)]
            for j in num:
                if j==0:
                    break
                if i%j!=0:
                    break
            else:
                ans.append(i)
        return ans