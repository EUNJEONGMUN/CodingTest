package Greedy.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class BOJ1339 {
    static int N;
    static List<String> arr = new ArrayList<>();
    static Integer[] point = new Integer[26];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            arr.add(br.readLine().trim());
        }

        for (int i = 0; i < point.length; i++) {
            point[i] = 0;
        }

        for (String word : arr) {
            for (int i = 0; i < word.length(); i++) {
                point[word.charAt(i) - 'A'] += (int) Math.pow(10, word.length() - i - 1);
            }

        }
        int number = 9;
        int answer = 0;

        Arrays.sort(point, Collections.reverseOrder());

        for (int v : point) {
            if (v == 0) {
                break;
            }
            answer += v * number--;
        }
        System.out.println(answer);
    }
}
