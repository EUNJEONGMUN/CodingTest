from typing import List
"""
https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
"""

class Solution:

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        answer = 0
        while (left < right):
            waterAmount = self.getWaterAmount(height, left, right)
            answer = max(answer, waterAmount)

            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return answer

    def getWaterAmount(self, height: List[int], x: int, y: int) -> int:
        return min(height[x], height[y]) * (y - x)


"""
인스턴스.메소드() 형태로 호출하게 되면 인스턴스가 메소드의 파라미터로 넘어가게 되기 때문에
메소드에 self 넣기

"""
