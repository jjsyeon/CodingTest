import java.util.*;
import java.io.*;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());

		for (int t = 1; t <= T; t++) {
			int answer = 0;
			int N = Integer.parseInt(br.readLine());
			int[] arr = new int[N+1];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= N; i++) arr[i] = Integer.parseInt(st.nextToken());
			int [] dp = new int[N+1];
			for (int i = 1; i<= N;i++) {
				dp[i] = 1;
				for (int j = 1;j<i;j++) {
					if (arr[j] < arr[i] && dp[i] < dp[j]+1) 
						dp[i] = dp[j]+1;
					answer = Math.max(answer, dp[i]);
				}
			}
			sb.append("#").append(t).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}
}
