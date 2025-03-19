
public class Solution {
    static int[] answer = {-1};
    static int[] visited = new int[11];
    static int[] apeech = new int[11];
    static int max = 0, arrow;


    public int[] solution(int n, int[] info) {
        for (int i = 0; i < 11; i++) apeech[i] = info[i];
        arrow = n;
        backtrack(0, 9);
        
        return answer;
    }

    public static void backtrack(int cnt, int idx ){
        if (cnt == arrow || idx < 0) {
            int diff = calc();
            if (max < diff) {
                max = diff;
                answer = visited.clone();
                answer[10] = arrow-cnt;
            }
            else if (diff == max && max != 0){
                visited[10] = arrow-cnt;
                for(int i = 10; i>= 0; i--){
                    if (answer[i] > visited[i]) return;
                    else if (answer[i] > visited[i]) break;
                }
                answer = visited.clone();
                visited[10] = 0;
            }
        }

        for (int i = idx; i >= 0; i--) {
            if (apeech[i] >= arrow - cnt) {continue;}
            visited[i] = apeech[i] + 1;
            backtrack(cnt + apeech[i] + 1, i-1);
            visited[i] = 0;
        }
    }

    public static int calc() {
        int score = 0;
        for (int i = 0; i < 11; i++) {
            if (visited[i] == 0 && apeech[i] == 0) continue;
            if (visited[i] > apeech[i]) score += (10 - i);
            else if (visited[i] <= apeech[i]) score -= (10 - i);
        }
        
        return score > 0? score:-1;
    }
}
