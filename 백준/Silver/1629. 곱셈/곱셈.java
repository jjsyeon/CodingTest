import java.io.*;
import java.util.*;

public class Main {
    static long A, B, C;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        A = Long.parseLong(st.nextToken());
        B = Long.parseLong(st.nextToken());
        C = Long.parseLong(st.nextToken());

        System.out.print(dnc(B));
    }
    static long dnc(long idx) {
        if (idx == 1) return A%C; // 재귀 탈출 조건
        long tmp = dnc(idx/2);
        return ((idx%2==0? 1:A%C) * (tmp * tmp % C))%C;
    }
}