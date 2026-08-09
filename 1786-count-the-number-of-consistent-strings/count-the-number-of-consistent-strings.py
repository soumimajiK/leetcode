class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            for j in range(len(i)):
                if i[j] not in allowed:
                    break
            else:
                count+=1
        return count