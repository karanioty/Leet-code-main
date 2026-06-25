'''3120. Count the Number of Special Characters I
""Example:
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters in word are 'a', 'b', and 'c'.'''
#code link: https://leetcode.com/problems/count-the-number-of-special-characters-i/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l=""
        l1=""
        count=0
        for i in word:
            if i in word.upper() and i not in l:
                l+=i
            elif i not in  l1:
                l1+=i
        
        for i in l:
            if i.lower() in l1:
                count+=1
        return count

        
        
