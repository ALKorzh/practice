class Solution(object):
    def mergeAlternately(self, word1, word2):
        s = []  
        len1, len2 = len(word1), len(word2)
        
        for i in range(min(len1, len2)):
            s.append(word1[i])
            s.append(word2[i])
        
        if len1 > len2:
            s.append(word1[len2:])
        else:
            s.append(word2[len1:])
        
        return ''.join(s)