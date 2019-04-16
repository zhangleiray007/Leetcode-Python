class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        rstr=""
        if len(a) == 0: return b
        if len(b) == 0: return a
        lens= len(a) if len(a) > len(b) else len(b)
        lenab=abs(len(a)-len(b))
        if len(a) > len(b):
            b=lenab*'0'+b
        elif len(a) < len(b):
            a = lenab * '0' + a
        addup=0
        while True:
            if a[-1]=='1' and b[-1]=='1' and addup==1:
                addup=1
                rstr = rstr +"1"
            elif a[-1]=='1' and b[-1]=='1' and addup==0:
                addup=1
                rstr = rstr +"0"
            elif a[-1] == '1' and b[-1] == '0' and addup == 1:
                addup=1
                rstr = rstr +"0"
            elif a[-1] == '1' and b[-1] == '0' and addup == 0:
                addup=0
                rstr = rstr +"1"
            elif a[-1] == '0' and b[-1] == '1' and addup == 1:
                addup=1
                rstr = rstr +"0"
            elif a[-1] == '0' and b[-1] == '1' and addup == 0:
                addup=0
                rstr = rstr +"1"
            elif a[-1] == '0' and b[-1] == '0' and addup == 1:
                addup=0
                rstr = rstr +"1"
            elif a[-1] == '0' and b[-1] == '0' and addup == 0:
                addup=0
                rstr = rstr +"0"
            lens =lens-1
            if lens==0 and addup ==0:
                return rstr[::-1]
            elif lens==0 and addup ==1:
                return '1'+rstr[::-1]
            else:
                a=a[0:-1]
                b=b[0:-1]
				
#  method 2				
class Solution:
	def addBinary(self, a, b):
		if len(a)==0: return b
		if len(b)==0: return a
		if a[-1] == '1' and b[-1] == '1':
			return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
		if a[-1] == '0' and b[-1] == '0':
			return self.addBinary(a[0:-1],b[0:-1])+'0'
		else:
			return self.addBinary(a[0:-1],b[0:-1])+'1'