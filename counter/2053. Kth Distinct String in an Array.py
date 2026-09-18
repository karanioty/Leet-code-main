'''2053. Kth Distinct String in an Array
""Example:
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. '''
#code link: https://leetcode.com/problems/kth-distinct-string-in-an-array/description/?envType=problem-list-v2&envId=counting
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        l=[]
        for i in arr:
            if arr.count(i)==1:
                l.append(i)
        print(l)
        if len(l)>=k:
            return l[k-1]
        else:
            return ""
