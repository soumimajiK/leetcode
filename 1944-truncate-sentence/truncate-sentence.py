class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sentence=s.split()
        ans=""
        for i in range(len(sentence)):
            if i!=k:
                ans+=sentence[i]+" "
            else:
                return ans.rstrip()
        return ans.rstrip()
        