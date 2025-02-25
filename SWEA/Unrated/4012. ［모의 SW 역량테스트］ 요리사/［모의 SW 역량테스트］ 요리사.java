import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
	static int  N, answer;
	static int [][] synergy;
	static boolean [] visited;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());
			synergy = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j <N;j++) synergy[i][j] = Integer.parseInt(st.nextToken());
 			}
			
			answer = Integer.MAX_VALUE;
			visited = new boolean[N];
			combination(0, 0);
			
			bw.write("#" + t + " " + answer + "\n");
		}
		bw.close();
	}
	
	static void combination(int idx, int length) {
		if (length == N/2) {
			answer = Math.min(answer, calcSynergy());
			return;
		}
		for (int i=idx;i<N;i++) {
			visited[i] = true;
			combination(i+1, length+1);
			visited[i] = false;
		}

	}
	
	static int calcSynergy() {
		int foodA = 0, foodB = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (visited[i] != visited[j] || i == j) continue;
				else if (visited[i]) foodA += synergy[i][j];
				else foodB += synergy[i][j];
			}
		}
		return Math.abs(foodA-foodB);
	}
}