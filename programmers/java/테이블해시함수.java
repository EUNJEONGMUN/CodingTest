package programmers.java;

import java.util.*;

public class 테이블해시함수 {

}

class 테이블해시함수_Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {

        Arrays.sort(data, (o1, o2) -> {
            if (o1[col-1] == o2[col-1]) {
                return o2[0]-o1[0];
            }
            return o1[col-1]-o2[col-1];
        });
        int answer = 0;
        for (int i=row_begin; i<=row_end; i++) {
            int si = 0;
            for (int j=0; j<data[i-1].length; j++) {
                si += (data[i-1][j]%(i));
            }
            answer = answer^si;
        }

        return answer;
    }
}


class 테이블해시함수2_Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {

        Arrays.sort(data, (o1, o2) -> {
            if (o1[col-1] == o2[col-1]) {
                return o2[0]-o1[0];
            }
            return o1[col-1]-o2[col-1];
        });

        int answer = 0;
        for (int i=row_begin; i<=row_end; i++) {
            int mod = i;
            int si = Arrays.stream(data[i-1])
            .map(j -> j%mod)
            .sum();
            answer = answer^si;
        }

        return answer;
    }
}