package Implementation.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ16935 {

    static int N, M, R;
    static int[][] board;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        board = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < R; i++) {
            solution(Integer.parseInt(st.nextToken()));
        }

        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                System.out.print(board[i][j]+" ");
            }
            System.out.println();
        }
    }

    private static void solution(int command) {
        switch (command) {
            case 1:
                upDown();
                break;
            case 2:
                leftRight();
                break;
            case 3:
                turnRight90();
                break;
            case 4:
                turnLeft90();
                break;
            case 5:
                turnGroupRight();
                break;
            case 6:
                turnGroupLeft();
                break;
        }
    }



    private static void upDown() {
        int n = board.length;
        for (int i=0; i<n/2; i++) {
            int[] temp = board[i];
            board[i] = board[n-i-1];
            board[n-i-1] = temp;
        }
    }

    private static void leftRight() {
        int n = board.length;
        int m = board[0].length;
        for (int i=0; i< n; i++) {
            for (int j=0; j<m/2; j++) {
                int temp = board[i][j];
                board[i][j] = board[i][m-j-1];
                board[i][m-j-1] = temp;
            }
        }
    }

    private static void turnRight90() {
        int n = board.length;
        int m = board[0].length;
        int[][] newBoard = new int[m][n];
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                newBoard[i][j] = board[n-1-j][i];
            }
        }
        board = newBoard;
    }

    private static void turnLeft90() {
        int n = board.length;
        int m = board[0].length;
        int[][] newBoard = new int[m][n];
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                newBoard[i][j] = board[j][m-1-i];
            }
        }
        board = newBoard;
    }

    private static void turnGroupRight() {
        int n = board.length;
        int m = board[0].length;
        int[][] newBoard = new int[n][m];
        for (int i=0; i<n/2; i++) {
            for (int j=0; j<m/2; j++) {
                newBoard[i][j] = board[i+n/2][j];
            }
        }

        for (int i=0; i<n/2; i++) {
            for (int j=m/2; j<m; j++) {
                newBoard[i][j] = board[i][j-m/2];
            }
        }

        for (int i=n/2; i<n; i++) {
            for (int j=m/2; j<m; j++) {
                newBoard[i][j] = board[i-n/2][j];
            }
        }

        for (int i=n/2; i<n; i++) {
            for (int j=0; j<m/2; j++) {
                newBoard[i][j] = board[i][j+m/2];
            }
        }

        board = newBoard;

    }

    private static void turnGroupLeft() {
        int n = board.length;
        int m = board[0].length;
        int[][] newBoard = new int[n][m];
        for (int i=0; i<n/2; i++) {
            for (int j=0; j<m/2; j++) {
                newBoard[i][j] = board[i][j+m/2];
            }
        }

        for (int i=0; i<n/2; i++) {
            for (int j=m/2; j<m; j++) {
                newBoard[i][j] = board[i+n/2][j];
            }
        }

        for (int i=n/2; i<n; i++) {
            for (int j=m/2; j<m; j++) {
                newBoard[i][j] = board[i][j-m/2];
            }
        }

        for (int i=n/2; i<n; i++) {
            for (int j=0; j<m/2; j++) {
                newBoard[i][j] = board[i-n/2][j];
            }
        }

        board = newBoard;
    }
}
