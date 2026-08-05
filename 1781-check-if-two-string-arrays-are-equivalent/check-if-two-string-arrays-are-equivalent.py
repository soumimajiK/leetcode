class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        fw1, fw2="", ""
        for i in word1:
            fw1+=i
        for j in word2:
            fw2+=j
        return fw1==fw2
        