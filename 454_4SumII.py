class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic={}
        for i in range(len(A)):
            for j in range(len(B)):
                temp=A[i]+B[j]
                if temp in dic:
                    dic[temp]=dic[temp]+1
                else:
                    dic[temp]=1
        count=0
        for i in range(len(C)):
            for j in range(len(D)):
                temp=-(C[i]+D[j])
                if temp in dic:
                    count=count+dic[temp]
                else:
                    continue
        return count