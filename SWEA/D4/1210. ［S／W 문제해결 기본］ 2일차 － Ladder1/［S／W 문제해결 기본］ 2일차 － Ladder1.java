import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int t = 0; t < 10; t++) { // 테스트 케이스 돌리기
            int T = Integer.parseInt(br.readLine()); // 테스트 케이스 입력
            int [][] map = new int[100][100];
            for (int i = 0; i < 100; i++) { // 사다리 타기 지도 입력
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 100; j++) {
                    map[j][i] = Integer.parseInt(st.nextToken());
                }
            }
            int x, y; // 움직이는 좌표
            for (int i = 0; i < 100; i++) {
                x = i;
                if (map[x][0] == 0) continue;
                y = 0;
                char direction = 'D';
                while (y < 99) {
                    if (direction != 'L' && x+1 < 100 && map[x+1][y] != 0) {
                        x++;
                        direction = 'R';
                    }// 오른쪽으로
                    else if (direction != 'R' && x-1 >=0 && map[x-1][y] != 0) {
                        x--;
                        direction = 'L';
                    }// 왼쪽으로
                    else {
                        y++;
                        direction = 'D';
                    }
                }
                if (map[x][99] == 2) {
                    System.out.printf("#%d %d\n", T, i);
                    break;
                }

            }
        }
    }
}