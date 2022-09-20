def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    rows = [''] * numRows
    row = 0
    goingDown = False
    for c in s:
        rows[row] += c
        if row == 0 or row == numRows - 1:
            goingDown = not goingDown
        row += 1 if goingDown else -1
    return ''.join(rows)
