class Solution:
    def compress(self, chars: List[str]) -> int:
        s=[]
        count=1
    
        l=len(chars)
        for i in range(0,l-1):
            if l==1:
                s.append(chars[i])
                break
            if chars[i]==chars[i+1]:
                count+=1
            if chars[i]!=chars[i+1]:
                s.append(chars[i])
                if count>1:
                    s.extend(list(str(count)))
                    count=1
        s.append(chars[-1])
        if count>1:
            s.extend(list(str(count)))
        
        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)