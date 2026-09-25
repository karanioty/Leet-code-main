'''60. Permutation Sequence
""Example:
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.'''
#code link: https://leetcode.com/problems/permutation-sequence/description/
#from itertools import permutations as pe
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a=[i for i in range(1,n+1)]
        c=1
        for i in permutations(a,len(a)):
            if c==k:
               return "".join(map(str,i))
            c+=1
          
