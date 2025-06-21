class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        r=list(s)
        e=list(t)
        m=len(s)
        n=len(t)
        count=0
        start=0
        for i in range(m):
            for j in range(start,n):
                if r[i]==e[j]:
                    count+=1
                    start=j+1
                    break

        if count==m:
            return True
        else:
            return False