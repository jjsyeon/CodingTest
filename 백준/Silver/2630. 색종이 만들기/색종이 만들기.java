import java.io.*;

public class Main {
    static int [][] paper;
    static int whitePaper, bluePaper;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st;
        String line;
        int N = Integer.parseInt(br.readLine());
        paper = new int [N][N];
        for (int i = 0; i < N; i++) {
            line = br.readLine();
            for (int j = 0; j < N; j++) paper[i][j] = line.charAt(j*2) == '1'? 1 : 0;
        }
        cntPaper(N, 0, 0);
        System.out.println(whitePaper);
        System.out.println(bluePaper);


    }
    static void cntPaper(int size, int x, int y) {
        boolean isSame = true;
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (paper[i][j] != paper[x][y]) {
                    isSame = false;
                    break;
                }
            }
        }
        if (isSame) {
            if (paper[x][y] == 1) bluePaper++;
            else whitePaper++;
            return;
        }
        cntPaper(size/2, x, y);
        cntPaper(size/2, x + size/2, y);
        cntPaper(size/2, x, y + size/2);
        cntPaper(size/2, x + size/2, y + size/2);
    }
}