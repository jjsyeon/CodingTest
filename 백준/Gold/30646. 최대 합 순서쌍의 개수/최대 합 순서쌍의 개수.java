import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] arr = new long[N + 1];
        long[] prefixSum = new long[N + 1];
        Map<Long, Integer> firstIdx = new HashMap<>();
        Map<Long, Integer> lastIdx = new HashMap<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Long.parseLong(st.nextToken());
            prefixSum[i] = prefixSum[i - 1] + arr[i];
            if (!firstIdx.containsKey(arr[i])) { firstIdx.put(arr[i], i); }
            lastIdx.put(arr[i], i);
        }
        int s, e, ansCnt = 0;
        long ansSum = -1, sum;
        for (long x : firstIdx.keySet()){
            s = firstIdx.get(x); e = lastIdx.get(x);
            sum = prefixSum[e] - prefixSum[s-1];

            if (sum > ansSum) {
                ansSum = sum;
                ansCnt = 1;
            }
            else if (sum == ansSum) {
                ansCnt++;
            }
        }
        System.out.printf("%d %d\n", ansSum, ansCnt);
    }
}