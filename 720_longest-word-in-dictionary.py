#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#
class Solution:
    def longestWord(self, words):
        if not words:
            return ""
        longestword=''
        wordset=set([''])
        words.sort()
        for word in words:
            if word[:-1] in wordset:
                wordset.add(word)
                if len(longestword)<len(word):
                    longestword=word
        return longestword
        
a=Solution()
word = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]
w=a.longestWord(word)
print(w)
