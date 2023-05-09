package programmers.java;

public class n제곱배열자르기 {

}
class n제곱배열자르기_Solution {
    static int[][] matrix;
    public int[] solution(int n, long left, long right) {
        int[] answer = new int[(int) (right-left+1)];
        matrix = new int[n][n];
        for (int i=0; i<n; i++) {
            fillMatrix(i);
        }

        for (long i=left; i<=right; i++) {
            answer[(int) (i-left)] = matrix[(int) (i/n)][(int) (i%n)];
        }
        return answer;
    }

    public void fillMatrix(int idx) {
        for (int x=0; x<idx; x++) {
            matrix[x][idx] = idx+1;
        }
        for (int y=0; y<idx+1; y++) {
            matrix[idx][y] = idx+1;
        }
    }
}