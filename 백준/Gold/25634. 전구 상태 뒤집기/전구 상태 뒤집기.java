import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[] luminosity, init, sum;
    static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        luminosity = new int[N];
        sum = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) luminosity[i] = Integer.parseInt(st.nextToken());

        init = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            init[i] = Integer.parseInt(st.nextToken());
            sum[i] = (i>0 ? sum[i-1] : 0) + init[i] * luminosity[i];
        }

        dp = new int[2][N];
        dp[0][0] = (init[0]+1) % 2 * luminosity[0];
        dp[1][0] = dp[0][0];

        int maxLight =  0;
        for (int i = 1; i < N; i++) {
            dp[0][i] = sum[i-1] + (init[i]+1)%2 * luminosity[i]; // 새로 뒤집는다
            dp[1][i] = Math.max(dp[0][i-1], dp[1][i-1]) + (init[i]+1)%2 * luminosity[i]; // 앞에 이어서 뒤집는다
            maxLight = Math.max(maxLight, Math.max(dp[0][i-1], dp[1][i-1]) + sum[N-1] - sum[i-1]); // 여기서 뒤집는 것 끝낸다
        }
        maxLight = Math.max(maxLight, Math.max(dp[0][N-1], dp[1][N-1]));
        System.out.println(maxLight);
    }
}