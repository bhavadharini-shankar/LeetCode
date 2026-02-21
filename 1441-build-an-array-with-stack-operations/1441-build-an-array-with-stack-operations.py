class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        l=len(target)
        j=0
        for i in range(1,n+1):
            if j==l:
                break
            else:
                s.append("Push")
                j+=1
                if i not in target:
                    s.append("Pop")
                    j-=1
        return s