package programmers.java;

public class 미로탈출명령어 {

    public static void main(String[] args) {
        미로탈출명령어_Solution solution = new 미로탈출명령어_Solution();
        String ans = solution.solution(3, 4, 2, 3, 3, 1, 5);
        System.out.println(ans);
    }
}

class 미로탈출명령어_Solution {

    int[] dx = {1, 0, 0, -1};
    int[] dy = {0, -1, 1, 0};
    char[] dir = {'d', 'l', 'r', 'u'};
    int N, M, R, C, K;
    StringBuilder sb = new StringBuilder();
    String answer = "impossible";

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        N = n;
        M = m;
        R = r - 1;
        C = c - 1;
        K = k;
        search(0, x - 1, y - 1, k);
        return answer;
    }

    private boolean search(int depth, int x, int y, int k) {
        if (depth == k) {
            if (x == R && y == C) {
                answer = sb.toString();
                return true;
            }
            return false;
        }
        boolean flag = false;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (checkRange(nx, ny) && (Math.abs(nx - R) + Math.abs(ny - C)) < k - depth
                && (Math.abs(nx - R) + Math.abs(ny - C)) % 2 == (k - depth + 1) % 2) {
                sb.append(dir[i]);
                if (search(depth + 1, nx, ny, k)) {
                    flag = true;
                    break;
                }
                sb.deleteCharAt(sb.length() - 1);
            }
        }
        return flag;
    }

    private boolean checkRange(int x, int y) {
        if (x >= 0 && x < N && y >= 0 && y < M) {
            return true;
        }
        return false;
    }
}