class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        nl = list(num)
        while nl[-1] == "0":
            nl.pop()
        return "".join(nl)