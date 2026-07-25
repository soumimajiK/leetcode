class Solution:
    def isPalindrome(self, x: int) -> bool:
        mylist=list(str(x))
        left=0
        right=len(mylist)-1
        while left<right:
            if mylist[left]==mylist[right]:
                left+=1
                right-=1
                continue
            else:
                return False
        return True
