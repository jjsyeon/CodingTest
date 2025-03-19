
public class Solution {
    int[] answer = {-1};
    int[] visited = new int[11];
    int[] apeech;
    int max = 0, arrow;

    public int[] solution(int n, int[] info) {
        apeech = info.clone();
        arrow = n;
        backtrack(0, 9);
        
        return answer;
    }

    public void backtrack(int cnt, int idx ){
        if (cnt == arrow || idx < 0) {
            int diff = calc();
            if (max < diff || (diff == max && answer[answer.length-1] < arrow-cnt)) {
                max = diff;
                answer = visited.clone();
                answer[10] = arrow-cnt;
            }
        }

        for (int i = idx; i >= 0; i--) {
            if (apeech[i] >= arrow - cnt) {continue;}
            visited[i] = apeech[i] + 1;
            backtrack(cnt + apeech[i] + 1, i-1);
            visited[i] = 0;
        }
    }

    public int calc() {
        int score = 0;
        for (int i = 0; i < 11; i++) {
            if (visited[i] == 0 && apeech[i] == 0) continue;
            if (visited[i] > apeech[i]) score += (10 - i);
            else if (visited[i] <= apeech[i]) score -= (10 - i);
        }
        
        return score > 0? score:-1;
    }
}
