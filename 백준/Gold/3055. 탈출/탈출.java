import java.util.*;
import java.io.*;

public class Main {
	static int R, C;
	static char[][] map;
	static int[][] visited;
	final static int[] dx = { -1, 1, 0, 0 }, dy = { 0, 0, -1, 1 };

	public static void main(String[] args) throws IOException {
		// 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		map = new char[R][C];
		String line;
		for (int r = 0; r < R; r++) {
			line = br.readLine();
			for (int c = 0; c < C; c++) map[r][c] = line.charAt(c);
		}
		
		// 방문 배열 초기화
		visited = new int[R][C];
		for (int r = 0; r < R; r++) Arrays.fill(visited[r], -1);
		
		// BFS를 위한 queue 초기화 -> 양방향으로 입력 가능한 queue가 필요하므로 deque 활용
		Deque<int[]> queue = new ArrayDeque<>();

		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (map[r][c] == '*') // 물이 차오른 지점 체크(시간 변화에 따라 주변에 퍼지니까 queue에 넣어 고려해줘야함)
					queue.addFirst(new int[] { r, c }); // 물이 찰 예정인 칸으로 고슴도치가 이동할 수 없으므로 queue의 앞에 추가해 고슴도치보다 물을 먼저 고려하도록 함
				else if (map[r][c] == 'S') { // 고슴도치 시작 지점 체크
					queue.addLast(new int[] { r, c });
					visited[r][c] = 0;
				}
			}
		}
		int[] curr;
		char currStat;
		while (!queue.isEmpty()) {
			curr = queue.poll();
			int x = curr[0], y = curr[1];
			currStat = map[x][y];
			for (int i = 0; i < 4; i++) {
				int mx = x + dx[i], my = y + dy[i];
				if (mx < 0 || R <= mx || my < 0 || C <= my) continue; // 이동할 위치가 map 범위 밖이면 넘어가기
				if (visited[mx][my] != -1) continue; // 이동하려는 위치에 이미 방문했다면 넘어가기
				if (map[mx][my] == '*' || map[mx][my] == 'X') continue; // 동할 위치가 물 or 돌이면 넘어가기
				if (currStat == '*' && map[mx][my] == 'D') continue; // 다음 위치가 비버 굴(최종 도착지)이면 물이 차오르지 않도록 함

				if (currStat == 'S') { // 고슴도치가 이동 경로 업데이트해주는 경우
					if (map[mx][my] == 'D') { // 이동할 위치가 비버 굴이면 종료 조건 만족
						System.out.println(visited[x][y] + 1);
					    return; 
					}
					visited[mx][my] = visited[x][y] + 1; // 얼마나 이동해서 도달했는지 업데이트
				}

				map[mx][my] = currStat; // 이동한 위치가 이전의 상태로 변함(물 차오르는 것, 고슴도치 이동한 것 모두 처리 가능)
 				queue.add(new int[] { mx, my });
			}
		}
		System.out.println("KAKTUS");
	}
}