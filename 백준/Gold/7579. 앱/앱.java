import java.util.*;
import java.io.*;

public class Main {
	static int N, M;
	static int[] memories;
	static int[] times;
	static int[][] dp;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		memories = new int[N + 1];
		times = new int[N + 1];
		int maxTime = 0;
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) memories[i] = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			times[i] = Integer.parseInt(st.nextToken());
			maxTime += times[i];
		}

		dp = new int[N + 1][maxTime + 1];
		int memory, cost;
		for (int n = 1; n <= N; n++) {
			memory = memories[n]; cost = times[n];
			for (int t = 0; t <= maxTime; t++) {
				if (t >= cost) dp[n][t] = Math.max(dp[n-1][t-cost]+memory, dp[n-1][t]);
				else dp[n][t] = dp[n-1][t];
			}
		}
		// lower bound 탐색
		int start= 0, end = maxTime, mid;
		while (start < end) {
			mid = (start + end) / 2;
			if (dp[N][mid] < M) start = mid+1;
			else end = mid;
		}
		
		System.out.println(end);
	}
}