class Solution(object):
    def longestCommonPrefix(self, strs):
        rstr=""
        strstmp=strs
        if strstmp==[]:
            return rstr
        elif len(strstmp)==1:
            return strstmp[0]
        else:
            while "" not in strstmp:
                flaga=0
                tmps=""
                d = {}
                for i in strstmp:
                    if i[0] in d:
                        d[i[0]].append(i)
                    else:
                        d[i[0]] = [i]
                    if len(i)==1:
                        flaga=1
                    tmps=i[0]
                if len(d) >1:
                    return rstr
                else:
                    rstr =rstr + tmps
                if flaga ==1:
                    return rstr
                else:
                    for i in range(len(d[tmps])):
                        d[tmps][i]=d[tmps][i][1::]
                strstmp = d[tmps]
            return rstr