import java.util.*;

class Solution {
    List<int[]>[] map;
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        map = new List[n+1];
        for (int i = 1; i<=n; i++) map[i] = new ArrayList<>();
        for (int[] f : fares) {
            int x = f[0], y = f[1], m = f[2];
            map[x].add(new int[] {y, m});
            map[y].add(new int[] {x, m});
        }
        
        int answer = Integer.MAX_VALUE;
        int[] distS = djk(s, n), distA = djk(a, n), distB = djk(b, n);
        for(int i = 1; i <= n; i++) {
            int tmp = distS[i] + distA[i] + distB[i];
            answer = answer < tmp ? answer : tmp;
        }

        return answer;
    }
    
    int[] djk(int start, int n) {
        int[] dist = new int[n+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        
        PriorityQueue<int[]> queue = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        queue.add(new int[] {start, 0});
        
        int[] curr;
        while (!queue.isEmpty()) {
            curr = queue.poll();
            int pos = curr[0], fare = curr[1];
            if (dist[pos] < fare) continue;
            dist[pos] = fare;
            for (int [] nxt : map[pos]) {
                if (dist[nxt[0]] <= fare + nxt[1]) continue;
                dist[nxt[0]] = fare + nxt[1];
                queue.add(new int[] {nxt[0], dist[nxt[0]]});
            } 

        }
        return dist;
    }
}