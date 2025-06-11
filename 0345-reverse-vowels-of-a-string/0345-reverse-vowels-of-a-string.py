class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        m=[]
        j=0
        b=list(s)
        for i in b:
            l.append(i)
            if i in ["a","e","i","o","u","A","E","I","O","U"]:
                m.append(i)
        m.reverse()
        for index in range(len(b)):
            if b[index] in ["a","e","i","o","u","A","E","I","O","U"]:
                l[index]=m[j]
                j+=1
        k="".join(l)

        return k
