class Solution:
 
    def getPermutation(self, n: int, k: int) -> str:
        result=''
        nums=['1','2','3','4','5','6','7','8','9']
        k=k-1
        factorial=1
        for i in range(1,n): factorial = factorial *i
        for i in reversed(range(n)):
            s=nums[int(k/factorial)]
            result=result+s
            nums.remove(s)
            if i!=0:
                k=k%factorial
                factorial=factorial/i
        return result