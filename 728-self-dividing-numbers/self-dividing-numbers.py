class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            num = i
            while num:
                digit=num%10
                if digit==0 or i%digit!=0:
                    break 
                num//=10
            else:
                ans.append(i)
        return ans 