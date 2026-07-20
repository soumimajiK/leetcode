class Solution:
    def defangIPaddr(self, address: str) -> str:
        newlist=list(address)
        for i in range(len(newlist)):
            if newlist[i]==".":
                newlist[i]="[.]"
        return "".join(newlist)
       
        