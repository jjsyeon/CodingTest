import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            int N = Integer.parseInt(br.readLine());
            String answer = "YES\n";
            String[] inputs = new String[N];
            for (int n = 0; n < N; n++) {
                inputs[n] = br.readLine();
            }
            Arrays.sort(inputs);
            for (int i = 0; i < N-1; i++){
                if (inputs[i+1].startsWith(inputs[i])) {
                    answer = "NO\n";
                    break;
                }
            }
            sb.append(answer);
        }
        System.out.println(sb);
    }
}
