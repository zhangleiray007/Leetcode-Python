class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one=0;two=0;three=0
        for i in nums:
            two |=(one & i)
            one ^=i
            three=~(one & two)
            one &=three
            two &=three
        return one
