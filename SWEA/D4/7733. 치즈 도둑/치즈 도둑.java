import java.io.*;
import java.util.*;

public class Solution {
    static StringTokenizer st;
    static int [] dx = {-1, 1, 0, 0};
    static int [] dy = {0, 0, -1, 1};
    static int [][] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        // 입력 받기
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t<=T; t++){
            int n = Integer.parseInt(br.readLine());
            int [][] table = new int[n][n];
            int minHeight = 101, maxHeight = 0;
            for (int x = 0; x < n; x++){
                st = new StringTokenizer(br.readLine());
                for (int y = 0; y < n; y++){
                    table[x][y] = Integer.parseInt(st.nextToken());
                    minHeight = Math.min(minHeight, table[x][y]);
                    maxHeight = Math.max(maxHeight, table[x][y]);
                }
            }

            int answer = 1;
            for (int h = minHeight; h < maxHeight; h++){
                visited = new int[n][n];
                int cnt = 0;
                for (int x = 0; x < n; x++){
                    for (int y = 0; y < n; y++){
                        if (visited[x][y] == 0 && table[x][y] > h){
                            cnt++;
                            // bfs 탐색
                            visited[x][y] = 1;
                            Queue<int[]> q = new LinkedList<>();
                            q.add(new int[]{x, y});
                            int[] cur;
                            while (!q.isEmpty()){
                                cur = q.poll();
                                for (int i = 0; i < 4; i++){
                                    int mx = cur[0]+dx[i], my = cur[1]+dy[i];
                                    if (mx>=0 && mx < n && my>=0 && my < n && visited[mx][my] == 0 && table[mx][my] > h){
                                        visited[mx][my] = 1;
                                        q.add(new int[]{mx,my});
                                    }
                                }
                            }
                        }
                        else visited[x][y] = 1;
                    }
                }
                if (cnt > answer) answer = cnt;
            }
            sb.append("#").append(t).append(" ").append(answer).append("\n");
        }
        System.out.println(sb);   
    }
}