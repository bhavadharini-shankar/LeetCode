class Solution:
    def mergeAlternately(self, word1: str, word2: str):
        result=""
        if len(word1)==len(word2):
            for a in range(len(word1)):
                result+=word1[a]+word2[a]
        else:
            min_len= min(len(word1),len(word2))
            for a in range(min_len):
                result+=word1[a]+word2[a]
            result+=word1[min_len:]+word2[min_len:]
             
        return result


