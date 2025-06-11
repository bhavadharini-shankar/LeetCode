class Solution:
    def reverseWords(self, s: str) -> str:
        m=s.split()
        m.reverse()
        k=" ".join(m)

        return k
