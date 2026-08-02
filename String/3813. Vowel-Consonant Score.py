'''3813. Vowel-Consonant Score
""Example:
Input: s = "cooear"
Output: 2
Explanation:
The string s = "cooear" contains v = 4 vowels ('o', 'o', 'e', 'a') and c = 2 consonants ('c', 'r').
The score is floor(v / c) = floor(4 / 2) = 2.'''
#code link: https://leetcode.com/problems/vowel-consonant-score/description/?envType=problem-list-v2&envId=string
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowel=0
        cons=0
        for i in s:
            if i in "aeiou":
                vowel+=1
            elif i not in "1234567890 ":
                cons+=1
        if cons!=0:
            return vowel//cons
        else:
            return 0
