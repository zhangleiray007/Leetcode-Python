class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) <sum(cost):
            return -1
        n = len(gas)
        totalcost = 0
        totalin = 0
        nCnt = 0
        temp=0
        gas.extend(gas[0:-1])
        cost.extend(cost[0:-1])
        gasseq=[]
        costseq=[]
        for i in range(len(gas)):
            gasseq.append(gas[i])
            costseq.append(cost[i])
            totalin = totalin + gas[i]
            totalcost = totalcost + cost[i]
            nCnt = nCnt + 1
            while totalin < totalcost:
                totalin = totalin - gasseq[0]
                totalcost = totalcost - costseq[0]
                del gasseq[0]
                del costseq[0]
                nCnt =nCnt-1
            if nCnt == n:
                return i - n+1
        return -1
                
