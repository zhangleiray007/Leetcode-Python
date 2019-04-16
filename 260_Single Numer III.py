class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from functools import reduce 
        res=[0,0]
        tmp=reduce(lambda x,y:x^y,nums)
        mask =tmp &(-tmp)        
        res[0]=reduce(operator.xor,list(filter(lambda x: x & mask,nums)))
        res[1]=tmp ^ res[0]
        return res
