class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet="abcdefghijklmnopqrstuvwxyz"
        new=sorted(set((sentence.lower())))
        return "".join(new)==alphabet
        