class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vert=0
        hor=0
        for i in moves:
            if i=="U":
                vert+=1
            elif i=="D":
                vert-=1
            elif i=="L":
                hor+=1
            elif i=="R":
                hor-=1
        return vert==0 and hor==0
        