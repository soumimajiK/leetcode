class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X=0
        for ops in operations:
            if ops=="++X" or ops=="X++":
                X+=1
            elif ops=="--X" or ops=="X--":
                X-=1
        return X
        