class Solution(object):
    def reverse(self, x):
        a=[]
        tmp=x
        out=0
        while tmp!=0:
            a.append(tmp%10)
            tmp=tmp/10
        for i in a:
            out=10*out+i
        if x<0:
            out=~out+1
        if out > 2**31 or out <-2**31:
            out=0
        return out

		
class Solution(object):
    def reverse(self, x):

        s=cmp(x,0);r=int(`s*x`[::-1]);return(r<2**31)*s*r

