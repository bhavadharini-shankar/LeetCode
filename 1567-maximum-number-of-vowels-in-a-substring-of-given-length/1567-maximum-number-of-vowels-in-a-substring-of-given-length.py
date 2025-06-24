class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        S=list(s)
        l=len(S)
        c=0
        max_c=0
        for i in range(k):
            if S[i] in ["a","e","i","o","u"]:
                c+=1
        max_c=c
        for i in range(k,l):
            if S[i] in ["a","e","i","o","u"]:
                c+=1
            if S[i-k] in ["a","e","i","o","u"]:
                c-=1
            if max_c<c:
                max_c=c
            
        return max_c