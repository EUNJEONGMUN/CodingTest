package BinarySearch.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ2110 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);

        int answer = 0;
        int minValue = 1;
        int maxValue = arr[arr.length - 1];


        while (minValue<=maxValue) {
            int mid = (minValue+maxValue)/2;

            if (setWIFI(mid, arr)>=C) {
                // C 보다 많이 설치했다면 -> 거리를 넓혀야 함.
                minValue = mid+1;
                answer = mid;
            } else {
                maxValue = mid-1;
            }
        }
        System.out.println(answer);
    }

    private static int setWIFI(int mid, int[] arr) {
        int cnt = 1;
        int lastSet = arr[0];
        for (int i=1; i<arr.length; i++) {
            if (arr[i]-lastSet>=mid) {
                cnt++;
                lastSet = arr[i];
            }
        }
        return cnt;
    }
}
