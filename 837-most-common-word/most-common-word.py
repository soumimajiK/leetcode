class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import string

        count={}
        mV=0
        mI=""
        translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
        arrA = paragraph.lower().translate(translator).split()
        for i in arrA:
            count[i]=count.get(i, 0) + 1
        for idx, val in count.items():
            if idx not in banned:
                if val>mV:
                    mV=val
                    mI=idx
        return mI