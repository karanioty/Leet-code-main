'''2108. Find First Palindromic String in the Array
""Example:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
'''
#code link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/?envType=problem-list-v2&envId=string
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        b=""
        for i in words:
            if i==i[::-1]:
                b=i
                break
        return b
        
