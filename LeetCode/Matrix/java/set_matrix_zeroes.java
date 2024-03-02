package LeetCode.Matrix.java;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/*
https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150
 */
public class set_matrix_zeroes {
    public void setZeroes(int[][] matrix) {
        Set<Integer> zeroCol = new HashSet<>();
        Set<Integer> zeroRow = new HashSet<>();

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    zeroRow.add(i);
                    zeroCol.add(j);
                }
            }
        }

        for (int row : zeroRow) {
            Arrays.fill(matrix[row], 0);
        }

        for (int col : zeroCol) {
            for (int i = 0; i < matrix.length; i++) {
                matrix[i][col] = 0;
            }
        }
        for (int[] m : matrix) {
            System.out.println(Arrays.toString(m));
        }
    }

    public void setZeroes2(int[][] matrix) {
        boolean isColumn = false;
        int R = matrix.length;
        int C = matrix[0].length;

        for(int i=0;i<R;i++){
            if(matrix[i][0] == 0){
                isColumn = true;
            }

            for(int j=1;j<C;j++){
                if(matrix[i][j] == 0){
                    matrix[0][j] =0;
                    matrix[i][0] =0;
                }
            }
        }

        for(int i=1;i<R;i++){
            for(int j=1;j<C;j++){
                if(matrix[i][0] == 0 || matrix[0][j]==0){
                    matrix[i][j] =0;
                }
            }
        }

        if (matrix[0][0] == 0) {
            for (int j = 0; j < C; j++) {
                matrix[0][j] = 0;
            }
        }

        // See if the first column needs to be set to zero as well
        if (isColumn) {
            for (int i = 0; i < R; i++) {
                matrix[i][0] = 0;
            }
        }

    }
}
