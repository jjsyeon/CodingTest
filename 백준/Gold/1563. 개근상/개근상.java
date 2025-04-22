import java.util.*;
import java.io.*;

public class Main {
    static final int MOD = 1_000_000;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        // 1) a[n] 계산
        int[] a = new int[N+1];
        a[0] = 1;
        if (N >= 1) a[1] = 2;
        if (N >= 2) a[2] = 4;
        for (int i = 3; i <= N; i++) {
            a[i] = ((a[i-1] + a[i-2]) % MOD + a[i-3]) % MOD;
        }
        // 2) L = 0
        int ans = a[N];
        // 3) L = 1, convolution
        for (int i = 0; i <= N-1; i++) {
            long ways = (long)a[i] * a[N-1-i] % MOD;
            ans = (ans + (int)ways) % MOD;
        }
        System.out.println(ans);
    }
}