class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        fres={}
        fret={}

        for c in s:
            fres[c] = fres.get(c,0)+1

        for c in t:
            fret[c] = fret.get(c,0)+1
        
        if fres==fret:
            return True
        return False



        