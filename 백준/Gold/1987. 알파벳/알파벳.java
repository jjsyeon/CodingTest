import java.io.*;
import java.util.*;

public class Main {
	static int [][] board;
	static int [] visited = new int [26];
	final static int [] dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};
	static int R, C, answer = 1;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		board = new int[R][C];
		
		for (int r = 0 ; r < R; r++) {
			line = br.readLine();
			for (int c = 0 ;c < C; c++) board[r][c] = line.charAt(c) - 'A';
		}
		dfs(0,0,0);
		System.out.println(answer);
	}
	
	static void dfs(int x, int y, int length) {
		visited[board[x][y]] = 1;
		length ++;
		int mx, my, cantGo = 0;
		for (int i = 0 ; i < 4; i ++) {
			mx = x + dx[i]; my = y + dy[i];
			if (mx < 0 || mx >= R || my < 0 || my >= C || visited[board[mx][my]] == 1) {
				cantGo++;
				continue;
			}
			dfs(mx,my,length);
			visited[board[mx][my]] = 0;
		}
		
		if (cantGo == 4) {
			answer = Math.max(answer, length);
		}
	}
}