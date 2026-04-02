class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1, -1, -1]  # for 'a', 'b', 'c'
        result = 0
        
        for i in range(len(s)):
            last[ord(s[i]) - ord('a')] = i
            
            # minimum index among last seen of a, b, c
            min_index = min(last)
            
            # add valid substrings
            result += (min_index + 1)
        
        return result