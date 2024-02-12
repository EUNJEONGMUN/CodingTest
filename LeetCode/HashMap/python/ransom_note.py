"""
https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphabet = [0] * 26
        for i in range(len(magazine)):
            alphabet[ord(magazine[i]) - ord('a')] += 1

        for i in range(len(ransomNote)):
            idx = ord(ransomNote[i]) - ord('a')
            if (alphabet[idx] == 0):
                return False
            alphabet[idx] -= 1
        return True
