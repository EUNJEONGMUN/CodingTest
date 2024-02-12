"""
https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)

        if (sLen > tLen):
            return False

        idx = 0
        for i in range(tLen):
            if (idx == sLen):
                break
            if (s[idx] == t[i]):
                idx += 1
        if (idx == sLen):
            return True
        return False


c = Solution()
print(c.isSubsequence("a", "aa")) # true
