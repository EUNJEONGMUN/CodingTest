package programmers.java;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class 폰켓몬 {

}

class 폰켓몬_Solution {

    public int solution(int[] nums) {
        Set<Integer> phonekemon = new HashSet<>();
        for (int num : nums) {
            phonekemon.add(num);
        }
        return Math.min(nums.length / 2, phonekemon.size());
    }
}

class 폰켓몬_Solution2 {

    public int solution(int[] nums) {
        return Math.min((int) Arrays.stream(nums).distinct().count(), nums.length/2);
    }
}