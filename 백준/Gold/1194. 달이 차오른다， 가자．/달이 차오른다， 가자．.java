import java.util.*;
import java.io.*;

public class Main {
	static int N, M;
	static char[][] map;
	static boolean[][][] visited;
	final static int[] dx = { -1, 1, 0, 0 }, dy = { 0, 0, -1, 1 };
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new char[N][M];
		int x = -1, y = -1;
		for (int n = 0; n < N; n++) {
			String line = br.readLine();
			for (int m = 0; m < M; m++) {
				map[n][m] = line.charAt(m);
				if (map[n][m] == '0') {
					x = n; y = m;
				}
			}
		}
		visited = new boolean[64][N][M];
		int answer = -1;
		Queue<int[]> queue = new ArrayDeque<>();
		queue.add(new int[] { x, y, 0, 0 });
		visited[0][x][y] = true;
		int[] curr;
		int dst, key, mx, my;
		while (!queue.isEmpty()) {
			curr = queue.poll();
			x = curr[0]; y = curr[1]; dst = curr[2]; key = curr[3];
			if (map[x][y] == '1') {
				answer = dst;
				break;
			}

			for (int i = 0; i < 4; i++) {
				mx = x + dx[i]; my = y + dy[i];
				if (mx < 0 || N <= mx || my < 0 || M <= my || map[mx][my] == '#' || visited[key][mx][my]) continue;
				else if (map[mx][my] == '.' || map[mx][my] == '0' || map[mx][my] == '1') {
                     visited[key][mx][my] = true;
                     queue.add(new int[] {mx, my, dst + 1, key});

                }
				else if (map[mx][my] >= 'a' &&  map[mx][my] <= 'z') {
					int nk = 1 << (map[mx][my] - 'a');
					nk = nk | key;
					if (visited[nk][mx][my]) continue;
					visited[nk][mx][my] = true;
					queue.add(new int[] {mx,my,dst+1, nk});
				}
				else if (map[mx][my] >= 'A' &&  map[mx][my] <= 'Z') {
					int door = 1 << (map[mx][my] - 'A');
					if ((key&door) >0) {
						visited[key][mx][my] = true;
						queue.add(new int[] {mx,my,dst+1,key});
					}
				}
			}
		}
		System.out.println(answer);
	}
}