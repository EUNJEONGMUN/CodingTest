package TwoPointer.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ1522 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();
        int answer = s.length();

        int aCount = (int) s.chars().filter(a -> a == 'a').count();

        // 원형 문자열을 푸는 방법

        // 방법1 -> 문자열 두 개 이어 붙이기
        s = s+s;
        for (int i = 0; i < s.length(); i++) {
            int bCount = 0;
            if (i+aCount >= s.length()) {
                break;
            }
            for (int j = i; j < i + aCount; j++) {
                if (s.charAt(j) == 'b') {
                    bCount++;
                }
            }
            answer = Math.min(answer, bCount);
        }

        // 방법 2 -> 문자열의 길이로 나누기
//        for (int i = 0; i < s.length(); i++) {
//            int bCount = 0;
//            for (int j = i; j < i + aCount; j++) {
//                if (s.charAt(j % s.length()) == 'b') {
//                    bCount++;
//                }
//            }
//            answer = Math.min(answer, bCount);
//        }
        System.out.println(answer);
    }
}
