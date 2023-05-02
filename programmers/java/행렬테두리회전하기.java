package programmers.java;

import java.util.ArrayList;
import java.util.List;

public class 행렬테두리회전하기 {

}

class 행렬테두리회전하기_Solution {

    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    int[][] matrix;

    public int[] solution(int rows, int columns, int[][] queries) {
        matrix = new int[rows + 1][columns + 1];
        int idx = 1;
        for (int i = 1; i < rows + 1; i++) {
            for (int j = 1; j < columns + 1; j++) {
                matrix[i][j] = idx++;
            }
        }
        List<Integer> answer = new ArrayList<>();
        for (int[] query : queries) {
            int minValue = rotate(query);
            answer.add(minValue);
        }

        return answer.stream().mapToInt(o -> o).toArray();
    }

    private int rotate(int[] query) {
        int minValue = matrix[query[0]][query[1]];
        int before = matrix[query[0]][query[1]];
        int x = query[0];
        int y = query[1];
        for (int i = 0; i < 4; i++) {
            while (checkRange(x + dx[i], y + dy[i], query)) {
                x += dx[i];
                y += dy[i];
                int temp = matrix[x][y];
                matrix[x][y] = before;
                before = temp;
                minValue = Math.min(minValue, temp);
            }
        }
        return minValue;
    }

    private boolean checkRange(int x, int y, int[] query) {
        if (x >= query[0] && y >= query[1] && x <= query[2] && y <= query[3]) {
            return true;
        }
        return false;
    }
}