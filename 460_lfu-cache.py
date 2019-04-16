#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#
# https://leetcode.com/problems/lfu-cache/description/
#
# algorithms
# Hard (28.51%)
# Total Accepted:    37.5K
# Total Submissions: 131.7K
# Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Frequently Used (LFU) cache.
# It should support the following operations: get and put.
# 
# 
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reaches its capacity, it should invalidate the least
# frequently used item before inserting a new item. For the purpose of this
# problem, when there is a tie (i.e., two or more keys that have the same
# frequency), the least recently used key would be evicted.
# 
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# LFUCache cache = new LFUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
#
class LFUCache:
    class Node:
        def __init__(self, key, value):
            self.value = value
            self.freq = 0

    def __init__(self, capacity: int):
        self.capacity, self.dict = capacity, {}
        self.feq_dict={}
        self.maxfeq=0

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            self.feq_dict[self.dict[key].freq].remove(key)
            if not self.feq_dict[self.dict[key].freq]:
                del self.feq_dict[self.dict[key].freq]
            self.dict[key].freq +=1
            if self.dict[key].freq in self.feq_dict:
                self.feq_dict[self.dict[key].freq].append(key)  
            else:
                self.feq_dict[self.dict[key].freq]=[key]
            if self.dict[key].freq  > self.maxfeq :
                self.maxfeq =  self.dict[key].freq
            return self.dict[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key].value = value
            self.feq_dict[self.dict[key].freq].remove(key)
            if not self.feq_dict[self.dict[key].freq]:
                del self.feq_dict[self.dict[key].freq]
            self.dict[key].freq +=1
            if self.dict[key].freq in self.feq_dict:
                self.feq_dict[self.dict[key].freq].append(key)  
            else:
                self.feq_dict[self.dict[key].freq]=[key]
            if self.dict[key].freq  > self.maxfeq :
                self.maxfeq =  self.dict[key].freq
        else:
            if len(self.dict) >= self.capacity: # remove the least recently used element
                for i in range(1,self.maxfeq+1):
                    if i in self.feq_dict:
                        key_tmp = self.feq_dict[i].pop(0)
                        if not self.feq_dict[i]:
                            del self.feq_dict[i]
                        break
                if len(self.dict) >=1:
                    del self.dict[key_tmp]
            if len(self.dict) < self.capacity and self.capacity != 0:
                self.dict[key] = self.Node(key, value)
                self.dict[key].freq +=1
                if self.dict[key].freq  > self.maxfeq :
                    self.maxfeq =  self.dict[key].freq
                if 1 in self.feq_dict:
                    self.feq_dict[1].append(key)
                else:
                    self.feq_dict[1]=[key]
            

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# cache = LFUCache(2)
# cache.put(1,1)
# cache.put(2,2)
# print(cache.get(1))
# cache.put(3, 3)
# print(cache.get(2))
# print(cache.get(3))
# cache.put(4, 4)
# print(cache.get(1))
# print(cache.get(3))
# print(cache.get(4))

# cache = LFUCache(3)
# cache.put(1,1)
# cache.put(2,2)
# cache.put(3,3)
# cache.put(4,4)
# print(cache.get(4))
# print(cache.get(3))
# print(cache.get(2))
# print(cache.get(1))
# cache.put(5, 5)
#
# print(cache.get(1))
# print(cache.get(2))
# print(cache.get(3))
# print(cache.get(4))
# print(cache.get(5))


cache = LFUCache(0)
cache.put(0,0)
print(cache.get(0))