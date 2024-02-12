from typing import List

"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        answer = []
        while (left < right):
            if (numbers[left] + numbers[right] == target):
                answer = [left + 1, right + 1]
                break
            if (numbers[left] + numbers[right] < target):
                left += 1
            else:
                right -= 1

        return answer
