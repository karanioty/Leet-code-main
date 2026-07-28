'''2942. Find Words Containing Character
""Example:
Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.'''
#code link: https://leetcode.com/problems/find-words-containing-character/description/?envType=problem-list-v2&envId=stringclass Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=[]
        for i in range(len(words)):
            if x in words[i]:
                l.append(i)
        return l
