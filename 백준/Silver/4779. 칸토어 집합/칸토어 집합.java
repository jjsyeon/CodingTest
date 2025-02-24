import java.io.*;
import java.util.*;

public class Main {
    static String[] history = new String[13];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        history[0] = "-";
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
        if (N == 0) return history[0];
        StringBuilder sb = new StringBuilder();
        if (history[N-1] == null) history[N-1] = dnc(N-1);
        return sb.append(history[N-1]).append(" ".repeat((int)(Math.pow(3, N-1)))).append(history[N-1]).toString();
    }
}