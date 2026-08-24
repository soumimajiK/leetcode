class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        morselist=[]

        for word in words:
            index=[]
            mlist=[]

            for letter in word:
                for i in range(len(alphabets)):
                    if alphabets[i]==letter:
                        index.append(i)
                        break

            for j in index:
                mlist.append(morse[j])
            morselist.append("".join(mlist))

        morselist = set(morselist)
        return len(morselist)