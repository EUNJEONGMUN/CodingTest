package Backtracking.java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;

public class BOJ2661 {
    static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        solution("");
    }

    private static void solution(String answer) {
        if (answer.length() == N) {
            System.out.println(answer);
            System.exit(0);
        }

        for (String str : List.of("1", "2", "3")) {
            if (canInsert(answer + str)) {
                solution(answer + str);
            }
        }
    }

    private static boolean canInsert(String str) {
        for (int len = 1; len <= str.length() / 2; len++) {
            if (str.substring(str.length() - (len * 2), str.length() - len)
                    .equals(str.substring(str.length() - len, str.length()))) {
                return false;
            }
        }
        return true;
    }
}