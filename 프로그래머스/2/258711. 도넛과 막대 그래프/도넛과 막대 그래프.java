import java.util.*;
import java.io.*;

class Solution {
    static Map<Integer, Set<Integer> []> graph = new HashMap<>();
    public int[] solution(int[][] edges) {
        int[] answer = new int[4];
        int from, to;
        for (int idx = 0; idx < edges.length; idx++){
            from = edges[idx][0]; to = edges[idx][1];
            if (!graph.containsKey(from)){
                Set<Integer> outSet = new HashSet<>();
                Set<Integer> inSet = new HashSet<>();
                graph.put(from, new Set[] {outSet, inSet});
            }
            if (!graph.containsKey(to)){
                Set<Integer> outSet = new HashSet<>();
                Set<Integer> inSet = new HashSet<>();
                graph.put(to, new Set[] {outSet, inSet});
            }
            graph.get(from)[0].add(to);
            graph.get(to)[1].add(from);

        }

        int tot = 0;
        for (int idx : graph.keySet()){
            if ((graph.get(idx)[1].isEmpty() || graph.get(idx)[1] == null) && graph.get(idx)[0].size() > 1) {
                tot = graph.get(idx)[0].size();
                answer[0] = idx;
            }
            else if (graph.get(idx)[0].size() == 2 && graph.get(idx)[1].size() >= 2) {
                answer[3]++;
            }
            else if (graph.get(idx)[0].isEmpty() || graph.get(idx)[0] == null) {
                answer[2]++;
            }
        }

        answer[1] = tot - answer[2] - answer[3];

        return answer;
    }
}