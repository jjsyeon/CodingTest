
import java.io.*;
import java.util.*;
	
public class Solution {
	static int T, N, M, K, answer;
	static int [][][] map;
	static Queue<int[]> q;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		 // 1 : 상 2: 하 3: 좌 4: 우
		T = Integer.parseInt(br.readLine());
		for (int t = 1 ; t <= T ; t++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			map = new int [N][N][3];
			q = new ArrayDeque<>();
			int x,y;
			for (int k = 0; k<K;k++) {
				st = new StringTokenizer(br.readLine());
				x = Integer.parseInt(st.nextToken()); y = Integer.parseInt(st.nextToken());
				map[x][y][0] = Integer.parseInt(st.nextToken());
				map[x][y][1] = Integer.parseInt(st.nextToken());
				map[x][y][2] = map[x][y][0];
				int [] v = {x,y};
				q.add(v);
			}
			while (M-- > 0) move();
			answer = 0;
			while (!q.isEmpty()) {
				int [] v = q.poll();
				answer += map[v[0]][v[1]][0];
			}
			sb.append("#").append(t).append(" ").append(answer).append("\n");
			
		}
		
		System.out.println(sb);
	}
	
	static void move() {
		int [][][] result = new int[N][N][3];
		int cnt = q.size();
		for(int i = 0 ; i < cnt; i++) {
			int [] v = q.poll();
			int micro = (int)map[v[0]][v[1]][0];
			int dir = map[v[0]][v[1]][1]; // map[v[0]][v[1]][1];
			map[v[0]][v[1]][2] = map[v[0]][v[1]][0];

            if (dir%10 == 1) {v[0]--;}
			else if (dir%10 == 2) {v[0]++;}
			else if (dir%10 == 3) {v[1]--;}
			else if (dir%10 == 4) {v[1]++;}

			if (result[v[0]][v[1]][0] == 0) {
				q.add(v);
				if (v[0] == 0 || v[0] == N-1 || v[1] == 0 || v[1] == N-1) {
					result[v[0]][v[1]][1] = dir%2==0 ? dir-1 : dir+1;
					result[v[0]][v[1]][0] += micro/2;
					result[v[0]][v[1]][2] = micro/2;
				}
				else {
					result[v[0]][v[1]][1] = dir;
					result[v[0]][v[1]][0] += micro;
					result[v[0]][v[1]][2] = micro;
				}
			}
			else {
				if (v[0] == 0 || v[0] == N-1 || v[1] == 0 || v[1] == N-1) {
					if (result[v[0]][v[1]][2] < micro/2) {
						result[v[0]][v[1]][2] = micro/2;
						result[v[0]][v[1]][1] = dir; 
					}
					result[v[0]][v[1]][1] = result[v[0]][v[1]][2] > micro/2 ? result[v[0]][v[1]][1] : (dir%2==0 ? dir-1 : dir+1);
					result[v[0]][v[1]][0] += micro/2;
				}
				else {
					if (result[v[0]][v[1]][2] < micro) {
						result[v[0]][v[1]][2] = micro;
						result[v[0]][v[1]][1] = dir; 
					}
					result[v[0]][v[1]][0] += micro;
				}
			}
//			
		}
		map = result;
	}
}
