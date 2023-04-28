package programmers.java;

import java.util.Arrays;

public class 이모티콘할인행사 {

    public static void main(String[] args) {
        이모티콘할인행사_Solution solution = new 이모티콘할인행사_Solution();
        int[] ans = solution.solution(new int[][]{{40, 10000}, {25, 10000}},
            new int[]{9000, 7000});
        System.out.println(Arrays.toString(ans));
    }
}
class 이모티콘할인행사_Solution {
    int[] discountPercents = {40, 30, 20, 10};
    int[][] usersStatic;
    int[] emoticonsStatic;
    int plusServiceMaxCount = 0;
    int saleMaxPrice = 0;

    public int[] solution(int[][] users, int[] emoticons) {
        usersStatic = users;
        emoticonsStatic = emoticons;
        createDiscountCombinations(0, new int[emoticonsStatic.length]);
        int[] answer = {plusServiceMaxCount, saleMaxPrice};
        return answer;
    }

    private void createDiscountCombinations(int depth, int[] discountCombination) {
        if (depth == emoticonsStatic.length) {
            int[] ret = getBuyPeopleAndPrice(discountCombination);
            if (plusServiceMaxCount < ret[0]) {
                plusServiceMaxCount = ret[0];
                saleMaxPrice = ret[1];
            } else if (plusServiceMaxCount == ret[0]) {
                saleMaxPrice = Math.max(saleMaxPrice, ret[1]);
            }
            return;
        }
        for (int i=0; i< discountPercents.length; i++) {
            discountCombination[depth] = discountPercents[i];
            createDiscountCombinations(depth+1, discountCombination);
        }
    }

    private int[] getBuyPeopleAndPrice(int[] discountCombination) {
        int plusServiceCount = 0;
        int salePrice = 0;
        for (int[] user : usersStatic) {
            int basePercent = user[0];
            int basePrice = user[1];

            int buyCost = 0;

            for (int i=0; i<emoticonsStatic.length; i++) {
                if (discountCombination[i] >= basePercent) {
                    buyCost += (emoticonsStatic[i]*((100-discountCombination[i])*0.01));
                }
            }
            if (buyCost >= basePrice) {
                plusServiceCount++;
            } else {
                salePrice+=buyCost;
            }
        }
        return new int[] {plusServiceCount, salePrice};
    }
}