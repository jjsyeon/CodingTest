import java.util.*;

class Solution {

    char[][] grid;
    int[] dx = {-1, 0, 1, 0};  // 상 우 하 좌
    int[] dy = {0, 1, 0, -1};

    // main entry
    public int[] solution(String[] grid) {
        int rows = grid.length;
        int cols = grid[0].length();

        this.grid = new char[rows][cols];
        for (int i = 0; i < rows; i++) {
            this.grid[i] = grid[i].toCharArray();
        }

        return findCycle(rows, cols);
    }

    // 모든 (행, 열, 방향) 상태에서 사이클 탐색
    public int[] findCycle(int rows, int cols) {
        List<Integer> cycleCount = new ArrayList<>();
        boolean[][][] visited = new boolean[rows][cols][4];  // (row, col, dir) 방문 여부

        // 모든 좌표 (row, col)와 모든 방향(dir)에 대해 순환 경로 탐색 시도
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                for (int dir = 0; dir < 4; dir++) {

                    // 해당 상태(위치 + 방향)를 이미 방문한 경우는 건너뜀
                    if (visited[row][col][dir]) continue;

                    // 방문하지 않은 경로면 trace()로 순환 경로 길이 추적
                    int cycleLength = trace(row, col, dir, visited, rows, cols);
                    cycleCount.add(cycleLength);
                }
            }
        }

        return cycleCount.stream()
                        .mapToInt(Integer::intValue)
                        .sorted()  // 오름차순 정렬
                        .toArray();
    }

    // 한 사이클을 추적하여 길이를 반환
    public int trace(int row, int col, int dir, boolean[][][] visited, int rows, int cols) {
        int count = 0;

        while (!visited[row][col][dir]) {
            visited[row][col][dir] = true;
            count++;

            // 현재 위치의 명령에 따라 방향 회전
            char c = grid[row][col];
            if (c == 'L') dir = (dir + 3) % 4;  // 좌회전
            else if (c == 'R') dir = (dir + 1) % 4;  // 우회전

            // 회전된 방향대로 한 칸 이동 (wrap-around)
            row = (row + dx[dir] + rows) % rows;
            col = (col + dy[dir] + cols) % cols;
        }

        return count;
    }
}