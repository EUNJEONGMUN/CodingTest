package Backtracking.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ12101 {
    static List<String> arr = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        solution(N, 0, new ArrayList<>());

        if (K > arr.size()) {
            System.out.println(-1);
        } else {
            System.out.println(arr.get(K-1));
        }
    }

    private static void solution(int n, int sum, List<String> res) {
        if (sum == n) {
            arr.add(String.join("+", res));
            return;
        } else if (sum > n) {
            return;
        }
        for (int elem : List.of(1, 2, 3)) {
            res.add(String.valueOf(elem));
            solution(n, sum + elem, res);
            res.remove(res.size() - 1);
        }
    }
}
