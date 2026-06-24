'''1768. Merge Strings Alternately
""Example:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r'''
#code link:  https://leetcode.com/problems/merge-strings-alternately/description/?envType=problem-list-v2&envId=string
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        r=""
        while(i<len(word1) and j<len(word2)):
            r+=word1[i]
            r+=word2[j]
            i+=1
            j+=1
        r+=word1[i:]+word2[j:]
        return r
