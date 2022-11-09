# Final Interview

## Problem
**LeetCode Problem 12 https://leetcode.com/problems/integer-to-roman/**

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

| Symbol   |      Value    | 
|:----------:|:-------------:|
|  I  |   1     |
|  V  |   5     |
|  X  |   10    |
|  L  |   50    |
|  C  |   100   |
|  D  |   500   |
|  M  |   1000  |


Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.

|   Symbol   |      Value    | 
|:------------:|:-------------:|
|      IV    |   4     |
|      I     |   9     |
|      X     |   40    |
|      XC    |   90    |
|      CD    |   400   |
|      CM    |   900   |


Given an integer, that is less then 3999, convert it to a roman numeral.


## Exemples

**Input:** 1996
**Output:** MCMCXVI

## Hints

1. Try to think of how a bruteforce solution would have to be
2. Fomulate increasing examples and observe theire equivalence to roman numerals. What is being added?
3. Can you represent all possibilities of decimals houses programmaticaly?
4. What operation would you have to do to each decimal house of the number in order to know if it is 1-9?



## Solution
In this method, we have to first observe the problem. The number given in the problem statement can be a maximum of 4 digits. The idea to solve this problem is: 
- Divide the given number into digits at different places like one's, two's, houndred's and thousand's
- Starting from the thousand’s place print the corresponding roman value. For example, if the digit at thousand’s place is 3 then print the roman equivalent of 3000.
- Repeat the second step until we reach one’s place.

Suppose the input number is 3549. So, starting from thousand’s place we will start printing the roman equivalent. In this case, we will print in the order as given below:
- The Roman equivalent of 3000
- The Roman equivalent of 500
- The Roman equivalent of 40
- The Roman equivalent of 9

This solution has a time and space complexity of O(1)