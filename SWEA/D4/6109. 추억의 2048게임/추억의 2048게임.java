import java.io.*;
import java.util.*;

public class Solution {
	static int [][] board;
	static int T, N;
	static String direction = null;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		T = Integer.parseInt(br.readLine());
		for (int t=1; t<=T; t++) {
			//입력 받기
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			direction = st.nextToken();
			board = new int[N][N];
			for (int r=0;r<N;r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0;c<N;c++) board[r][c] = Integer.parseInt(st.nextToken());
			}
			
			// 타일 이동
			if (direction.equals("up")) {rotation(0); play(); rotation(1);}
			else if (direction.equals("down")) {rotation(1); play(); rotation(0);}
			else if (direction.equals("left")) {play();}
			else if (direction.equals("right")) {rotation(1); rotation(1); play(); rotation(1); rotation(1);}
			
			// 결과 출력
			sb.append("#").append(t).append("\n");
			for (int r=0;r<N;r++) {
				for (int c=0;c<N;c++) sb.append(board[r][c]).append(" ");
				sb.append("\n");
			}
		}
		System.out.println(sb);
		
	}
	
	// 타일 이동 (left)
	static void play() {
		int cnt,s,e;
		int [][] result = new int [N][N];
		for (int r=0;r<N;r++) {
			cnt = 0; s = 0 ; e = 1;
			while (s < N && e < N) {
				if (board[r][s] == 0) {s++; e=s+1;}
				else if (board[r][e] == 0) {e++;}
				else if (board[r][s] == board[r][e]) {
					result[r][cnt++] = 2*board[r][s];
					s = e+1; e = s+1;
				}
				else {
					result[r][cnt++] = board[r][s];
					s = e; e = s+1;
				}
			}
			if (s < N) result[r][cnt++] = board[r][s];
		}
		board = result;
	}
	
	// 타일 회전
	static void rotation(int dir) {
		int [][] rotated = new int[N][N];
		if (dir == 1) { //오른쪽 회전
			for (int r = 0;r<N;r++) {
				for (int c = 0; c<N; c++) rotated[c][N-1-r] = board[r][c];
			}
		}
		else { // 왼쪽 회전
			for (int r = 0;r<N;r++) {
				for (int c = 0; c<N; c++) rotated[N-1-c][r] = board[r][c];
			}
		}
		board = rotated;
	}
}
