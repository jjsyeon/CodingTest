import java.util.*;
import java.io.*;

class Island{
    int idx, root;
    List<int[]> pos;

    Island(int idx){
        this.idx = idx;

        this.root = idx;
        this.pos = new ArrayList<>();
    }
}

class Bridge implements Comparable<Bridge>{
    int from, to;
    int weight;

    Bridge(int f, int s, int w){
        this.from = f;
        this.to = s;
        this.weight = w;
    }

    @Override
    public int compareTo(Bridge b) {
        return Integer.compare(this.weight, b.weight);
    }

}

public class Main {
    static int N, M, cnt = 0;
    static int[][] map;
    final static int[] dx = { -1, 0, 1, 0 }, dy = { 0, -1, 0, 1 };
    static List<Island> islands = new ArrayList<>();
    static List<Bridge> bridges = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        islands.add(null);
        for (int n = 0; n < N; n++) {
            st = new StringTokenizer(br.readLine());
            for (int m = 0; m < M; m++) {
                int val = Integer.parseInt(st.nextToken());
                if (val == 0) continue;
                map[n][m] = -1;
            }
        }
        // 섬 인덱스화
        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                if (map[n][m] >= 0) continue;
                islands.add(new Island(++cnt));
                check(n, m);
            }
        }

        // 다리 먼저 짓기
        for (Island island : islands) {
            if (island == null) continue;
            for (int[] v : island.pos) {
                buildBridge(v[0], v[1]);
            }
        }

        if (bridges.isEmpty()) {
            System.out.println(-1);
            return;
        }

        Collections.sort(bridges);

        int totDist = 0;

        for (Bridge bridge : bridges) {
            if (union(bridge.from, bridge.to)) {
                totDist += bridge.weight;
                cnt--;
                if (cnt == 1) {
                    System.out.println(totDist);
                    return;
                }
            }
        }
        System.out.println(-1);
    }

    static void check(int x, int y) {
        map[x][y] = cnt;
        islands.get(cnt).pos.add(new int[]{x, y});

        for (int i = 0; i < 4; i++) {
            int mx = x + dx[i], my = y + dy[i];
            if (mx < 0 || N <= mx || my < 0 || M <= my || map[mx][my] >= 0) continue;
            check(mx, my);
        }
    }

    static void buildBridge(int x, int y){
        int from = map[x][y], to;
        for (int i = 0; i < 4; i++){
            int mx = x, my = y;
            int dist = 0;
            to = -1;
            while (true) {
                mx += dx[i]; my += dy[i];
                if (mx < 0 || N <= mx || my < 0 || M <= my || map[mx][my] == from) break;
                if (map[mx][my] == 0) dist++;
                if (map[mx][my] >= 1) {to = map[mx][my]; break;}
            }
            if (dist > 1 && to > from) bridges.add(new Bridge(from, to, dist));
        }
    }

    static int find(int i) {
        if (islands.get(i).root == islands.get(i).idx)
            return islands.get(i).idx;
        return islands.get(i).root = find(islands.get(i).root);
    }

    static boolean union(int i1, int i2) {
        int x = find(i1);
        int y = find(i2);
        if (x == y) return false;
        islands.get(Math.max(x,y)).root = Math.min(x,y);
        return true;
    }
}