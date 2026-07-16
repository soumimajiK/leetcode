class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        paragraph = "".join([c.lower() if c.isalnum() else " " for c in paragraph])
        words = paragraph.split()
        print(words)

        hs = {}
        mxf, mxw = 0, None

        for w in words:
            if w in banned:
                continue
            hs[w] = hs.get(w, 0) + 1
            if hs[w] > mxf:
                mxf = hs[w]
                mxw = w

        return mxw
