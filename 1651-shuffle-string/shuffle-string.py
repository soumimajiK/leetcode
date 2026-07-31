class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newlist=[0]*len(s)
        for i in range(len(indices)):
                newlist[indices[i]]=s[i]
        return "".join(newlist)