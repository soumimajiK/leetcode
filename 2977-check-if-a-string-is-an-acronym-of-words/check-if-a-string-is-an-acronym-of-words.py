class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        compare=""
        for i in words:
            compare+=i[0]
        return compare==s
        