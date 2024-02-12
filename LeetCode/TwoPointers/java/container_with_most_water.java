package LeetCode.TwoPointers.java;

/*
https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
 */
public class container_with_most_water {
    /**
     * 기둥의 크기가 작은 경우가 변할 때 갱신되므로, left와 right의 크기를 비교하여 더 작은 쪽을 움직인다.
     */
    public static void main(String[] args) {
        System.out.println(maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7})); // 49
    }

    public static int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int answer = 0;

        while (left < right) {
            answer = Math.max(answer, getWaterAmount(height, left, right));

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return answer;

    }

    private static int getWaterAmount(int[] height, int x, int y) {
        return Math.min(height[x], height[y]) * (y - x);
    }
}
