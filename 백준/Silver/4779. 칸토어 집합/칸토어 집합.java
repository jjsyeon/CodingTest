import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        while (true) {
            try {
                int N = Integer.parseInt(br.readLine());
                sb.append(dnc(N)).append("\n");
            } catch (Exception e) {
                break;
            }
        }
        System.out.println(sb);
    }

    static String dnc(int N) {
        if (N == 0) return "-";
        StringBuilder sb = new StringBuilder();
        String tmp = dnc(N-1);
        return sb.append(tmp).append(" ".repeat((int)(Math.pow(3, N-1)))).append(tmp).toString();
    }
}