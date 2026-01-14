class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                i = "FizzBuzz"
                answer.append(i)
            elif i%3==0:
                i = "Fizz"
                answer.append(i)
            elif i%5==0:
                i = "Buzz"
                answer.append(i)
            else:
                answer.append(str(i))
            
        return answer