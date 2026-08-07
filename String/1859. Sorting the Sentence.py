'''1859. Sorting the Sentence
""Example:
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.'''
#code link: https://leetcode.com/problems/sorting-the-sentence/description/?envType=problem-list-v2&envId=string
class Solution:
    def sortSentence(self, s: str) -> str:
        p=[""]*(len(s.split()))
        for i in s.split():
            index=int(i[-1])-1
            p[index]=i[:len(i)-1]
        return ' '.join(p)
