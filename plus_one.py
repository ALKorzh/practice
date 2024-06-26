class Solution(object):
    def plusOne(self, digits):
        digits = [str(i) for i in digits]
        dig = ''
        for k in digits:
            dig += k
        dig = str(int(dig) + 1)
        digits = (int(i) for i in dig)
        return list(digits)