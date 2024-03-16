package Math.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ2525 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().trim().split(" ");
        int hour = Integer.parseInt(input[0]);
        int minute = Integer.parseInt(input[1]);
        int add = Integer.parseInt(br.readLine());

        System.out.println((hour + (minute + add) / 60) % 24 + " " + (minute + add) % 60);
    }
}
