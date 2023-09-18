package Backtracking.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

public class BOJ7490 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        for (int i = 0; i < TC; i++) {
            int N = Integer.parseInt(br.readLine());
            String[] arr = new String[N + N];
            int number = 1;
            for (int k = 0; k < arr.length; k += 2) {
                arr[k] = String.valueOf(number++);
            }
            arr[arr.length - 1] = "+";
            solution(1, arr);
            System.out.println();
        }
    }

    private static void solution(int idx, String[] arr) {
        if (idx == arr.length - 1) {
            if (sum(arr) == 0) {
                for (int i=0; i<arr.length-1; i++) {
                    System.out.print(arr[i]);
                }
                System.out.println();
            }
            return;
        }
        for (String op : List.of(" ", "+", "-")) {
            arr[idx] = op;
            solution(idx + 2, arr);
        }
    }

    private static int sum(String[] arr) {
        int res = 0;
        int temp = 0;
        String tempOp = "+";
        for (int i = 0; i < arr.length; i++) {
            try {
                temp = temp * 10 + Integer.parseInt(arr[i]);

            } catch (NumberFormatException e) {
                if (arr[i].equals(" ")) {
                    continue;
                }
                if (tempOp.equals("+")) {
                    res += temp;
                } else if (tempOp.equals("-")) {
                    res -= temp;
                }
                tempOp = arr[i];
                temp = 0;
            }
        }
        return res;
    }
}
