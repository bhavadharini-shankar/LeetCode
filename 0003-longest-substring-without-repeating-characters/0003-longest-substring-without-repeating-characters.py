class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        left=0
        max_length=0

        for a in range(len(s)):
            while s[a] in char_set:
                char_set.remove(s[left])
                left+=1

            char_set.add(s[a])

            max_length=max(max_length, a-left+1)

        return max_length
