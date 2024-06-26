class Solution(object):
    def isAnagram(self, s, t):
        s = sorted([i for i in s])
        t = sorted([i for i in t])
        return s == t