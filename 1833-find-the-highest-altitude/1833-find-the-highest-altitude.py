class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=len(gain)
        p=[]
        add=0
        p.append(0)
        for i in range(l):
            add+=gain[i]
            p.append(add)
        return max(p)