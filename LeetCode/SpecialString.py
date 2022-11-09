class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        res = []
        for i, c in enumerate(s):
            if c == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(s[1:i]) + '0')
                s = s[i + 1:]
        return ''.join(sorted(res)[::-1]) or s
