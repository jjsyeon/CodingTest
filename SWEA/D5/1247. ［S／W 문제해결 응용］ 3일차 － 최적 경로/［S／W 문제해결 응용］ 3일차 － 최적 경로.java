import java.io.*;
import java.util.*;

public class Solution {
	static int T, N, answer, cnt; 
	static int [] home = new int[2], company = new int[2], visited;
	static int [][] map, graph;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			map = new int [N+2][2];
			for (int i = 0; i < N+2; i++) {
				map[i][0] = Integer.parseInt(st.nextToken()); 
				map[i][1] = Integer.parseInt(st.nextToken());
			}
			graph = new int [N+2][N+2];
			for (int x = 0; x < N+2; x++) {
				for (int y = 0; y < N+2; y++) {
					if (x == y || graph[x][y] > 0) continue;
					graph[x][y] = graph[x][y] = Math.abs(map[x][0] - map[y][0]) + Math.abs(map[x][1] - map[y][1]);
				}	
			}

			answer = 200 * N;
			visited = new int[N+2];
			cnt = 0;
			dfs(0,0);
			sb.append("#").append(t).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}
	
	static void dfs(int start, int length) {
		visited[start] = 1; cnt++;
		if (length >= answer) return;
		if (cnt == N+1) {
			length += graph[start][1];
			answer = Math.min(answer, length);
			return;
		}
		for (int i = 2; i < N+2; i++) {
			if (visited[i] == 0) {
				dfs(i, length+graph[start][i]);
				visited[i] = 0;
				cnt--;
			}
		}
	}
}