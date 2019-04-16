class Solution(object):
    def isPalindrome(self, x):
        temp=abs(x)
        out=0
        while temp>0:
            out=10*out+temp%10
            temp=temp/10
        if out==abs(x) and x >=0:
            return True
        else: 
            return False


class Solution(object):
    def isPalindrome(self, x):
        if(x<0 or (x%10==0 and x!=0)):
            return False
        out =0
        while x>out:
            out =out *10 +x%10
            x/=10
        return x==out or x== out/10