class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] =='0': return 0
        prev =0
        cur =1
        n =len(s)
        for i in range(1,n+1):
            if s[i-1]=='0':
                cur =0
            if i<2 or  not (s[i-2] =='1' or (s[i-2]=='2' and s[i-1]<='6')):
                prev =0
            tmp =cur
            cur = cur + prev
            prev =tmp
            
        return cur