package Math.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ30923 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] numbers = new int[N];
        int idx = 0;
        for (String n : br.readLine().trim().split(" ")) {
            numbers[idx++] = Integer.parseInt(n);
        }

        long answer = numbers[0] * 2; // 위아래 넓이

        for (int i = 1; i < N; i++) {
            answer += (numbers[i] * 2); // 앞뒤 넓이
            if (numbers[i - 1] != numbers[i]) {
                answer += Math.abs(numbers[i] - numbers[i - 1]);
            }
        }
        System.out.println(answer + (N * 2) + numbers[0] + numbers[N - 1]);
    }
}
