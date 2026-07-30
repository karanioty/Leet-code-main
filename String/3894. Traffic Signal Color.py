'''3894. Traffic Signal Color
""Example:
Input: timer = 60
Output: "Red"
Explanation:
Since timer = 60, and 30 < timer <= 90, the answer is "Red".'''
#code link: https://leetcode.com/problems/traffic-signal-color/description/?envType=problem-list-v2&envId=string
class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer==0:
            return "Green"
        elif timer==30:
            return "Orange"
        elif 30<timer<=90:
            return "Red"
        else:
            return "Invalid"
