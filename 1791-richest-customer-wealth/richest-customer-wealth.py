class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxsum=0
        for i in range(len(accounts)):
            sumarr=0
            for j in range(len(accounts[i])):
                sumarr+=accounts[i][j]
            if sumarr>maxsum:
                maxsum=sumarr
        return maxsum