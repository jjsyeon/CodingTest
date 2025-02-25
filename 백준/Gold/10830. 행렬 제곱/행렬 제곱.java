import java.io.*;
import java.util.*;

public class Main {
    static int A;
    static int [][] matrix;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        long B = Long.parseLong(st.nextToken());
        matrix = new int [A][A];
        for (int i = 0; i < A; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < A; j++) matrix[i][j] = Integer.parseInt(st.nextToken()) % 1000;
        }
        matrix = powMatrix(B);
        for (int i = 0; i < A; i++) {
            for (int j = 0; j < A; j++)
                sb.append(matrix[i][j]).append(" ");
            sb.append("\n");
        }
        System.out.println(sb);
    }
    static int[][] powMatrix(long exponent) {
        if (exponent == 1) return matrix;
        else if (exponent == 2) return mulMatrix(matrix, matrix);
        else {
            int[][] tmp = powMatrix(exponent / 2);
            return exponent%2 == 0 ? mulMatrix(tmp, tmp) : mulMatrix(matrix, mulMatrix(tmp, tmp));
        }
    }

    static int[][] mulMatrix(int[][] m1, int[][] m2) {
        int[][] result = new int[A][A];
        for (int i = 0; i < A; i++){
            for (int j = 0; j < A; j++){
                for (int k = 0; k < A; k++) result[i][j] += m1[i][k] * m2[k][j];
                result[i][j] %= 1000;
            }
        }
        return result;
    }
}