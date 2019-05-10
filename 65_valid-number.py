#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip(' ')
        if len(s)==0:
            return False
        e_flag=-1;e_postion=-1
        plusneg_flag=-1
        point_flag=-1
        num_flag=-1
        front_flag=-1
        hasnum_flag=-1
        neednum_flag=-1
        Ps=0
        if len(s)==1:
            if s[Ps] >= '0' and  s[Ps] <= '9':
                return True
            else:
                return False
        while Ps < len(s):
            if (s[0]=='+' or s[0]=='-') and Ps == 0:
                Ps +=1
                num_flag =-1
                front_flag = 1
                continue
            elif s[Ps] >= '0' and  s[Ps] <= '9':
                Ps +=1
                hasnum_flag=1
                num_flag = 1
                if neednum_flag ==1:
                    neednum_flag=-1
            elif e_flag==-1 and s[Ps] == 'e':
                if Ps!=0 and Ps!=len(s)-1 and num_flag==1:
                    e_postion=Ps
                    num_flag = -1
                    Ps +=1
                    e_flag =1
                else:
                    return False
            elif  point_flag==-1 and  s[Ps] == '.':
                if  e_flag==-1 and (Ps==0 or num_flag==1 or (front_flag==1 and Ps==1)):
                    point_flag =1
                    Ps +=1
                    if num_flag==1:
                        num_flag = 1
                    else:
                        num_flag = -1
                else:
                    return False
            elif  plusneg_flag==-1 and (s[Ps] == '-' or s[Ps] == '+'):
                if e_flag ==1 and e_postion == Ps-1:
                    plusneg_flag =1
                    num_flag = -1
                    neednum_flag=1
                    Ps +=1
                else:
                    return False
            else:
                return False
        if Ps==len(s) and hasnum_flag==1 and neednum_flag!=1:
            return True
        else:
            return False

a=Solution()
w=a.isNumber(" 005047e+6")
print(w)

