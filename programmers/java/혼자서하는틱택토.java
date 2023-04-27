package programmers.java;

public class 혼자서하는틱택토 {

    public static void main(String[] args) {
        혼자서하는틱택토_Solution solution = new 혼자서하는틱택토_Solution();
        int ans = solution.solution(new String[]{"O.X", ".O.", "..X"});
        System.out.println(ans);
    }

}

class 혼자서하는틱택토_Solution {

    int[][] winPositions = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
        {0, 4, 8}, {2, 4, 6}};

    public int solution(String[] board) {
        String boardString = "";
        for (String s : board) {
            boardString += s;
        }

        int O_count = countShape("O", boardString);
        int X_count = countShape("X", boardString);

        // O가 X와 같거나 하나 많아야 한다.
        if (!(O_count == X_count || O_count == X_count + 1)) {
            return 0;
        }

        boolean O_win = isWin("O", boardString);
        boolean X_win = isWin("X", boardString);

        // 둘이 동시에 이길 수 없다.
        if (O_win && X_win) {
            return 0;
        }

        // X가 이길 때는 둘의 개수가 같아야 하고, O가 이길 때는 O의 개수가 더 많아야 한다.
        if (X_win && O_count > X_count || O_win && X_count >= O_count) {
            return 0;
        }
        return 1;
    }

    private int countShape(String shape, String board) {
        int count = 0;
        String[] split = board.split("");
        for (int i = 0; i < split.length; i++) {
            if (split[i].equals(shape)) {
                count++;
            }
        }
        return count;
    }

    private boolean isWin(String shape, String board) {
        String[] split = board.split("");
        for (int[] p : winPositions) {
            if (split[p[0]].equals(shape) && split[p[1]].equals(shape) && split[p[2]].equals(
                shape)) {
                return true;
            }
        }
        return false;
    }
}