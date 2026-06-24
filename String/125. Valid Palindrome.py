'''125. Valid Palindrome
""Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.""
'''
# code link: https://leetcode.com/problems/valid-palindrome/description/?envType=problem-list-v2&envId=string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        r=""
        for i in s:
            if i in a:
                r+=i.lower()
        
        return r==r[::-1]
        
        
