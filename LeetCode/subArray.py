class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = set()
        cur = set()
        for a in arr:
            cur = {a | b for b in cur} | {a}
            res |= cur
        return len(res)
