class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not set(words[i]) & set(words[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res
