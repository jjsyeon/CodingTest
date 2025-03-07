import java.io.*;
import java.util.*;

public class Solution {
	static int T, H, W, N, x, y;
	static char [][] map;
	static int [] dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer  st;
		StringBuilder sb = new StringBuilder();
		String line;
		T = Integer.parseInt(br.readLine());
		for (int t=1;t<=T;t++) {
			st = new StringTokenizer(br.readLine());
			H = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			map = new char [H][W];
			for (int h=0;h<H;h++) {
				line = br.readLine();
				for (int w=0;w<W;w++) {
					map[h][w] = line.charAt(w);
					if (map[h][w] == '^' || map[h][w] == 'v' ||map[h][w] == '>' ||map[h][w] == '<') {x = h; y = w;} 
				}
			}
			N = Integer.parseInt(br.readLine());
			line = br.readLine();
			for (int i = 0; i<N; i++) play(line.charAt(i));
			
			sb.append("#").append(t).append(" ");
			for (int h=0;h<H;h++) {
				for (int w=0;w<W;w++) {
					sb.append(map[h][w]);
				}
				sb.append("\n");
			}	
		}
		System.out.println(sb);
	}
	
	static void play(char command) {
		if (command == 'U') {
			if (x-1 >= 0 && map[x-1][y] == '.') map[x--][y] = '.';
			map[x][y] = '^';
		}
		else if (command == 'D') {
			if (x+1 < H && map[x+1][y] == '.') map[x++][y] = '.';
			map[x][y] = 'v';
		}
		else if (command == 'L') {
			if (y-1 >= 0 && map[x][y-1] == '.') map[x][y--] = '.';
			map[x][y] = '<';
		}
		else if (command == 'R') {
			if (y+1 < W && map[x][y+1] == '.') map[x][y++] = '.';
			map[x][y] = '>';
		}
		else if (command == 'S') {
			if (map[x][y] == '^') {
				for (int i=1;i<=x;i++) {
					if (map[x-i][y] == '.' || map[x-i][y] == '-') continue;
					else if (map[x-i][y] == '*') {map[x-i][y] = '.'; break;}
					else break;
				}
			}
			else if (map[x][y] == 'v') {
				for (int i=1;i<H-x;i++) {
					if (map[x+i][y] == '.' || map[x+i][y] == '-') continue;
					else if (map[x+i][y] == '*') {map[x+i][y] = '.'; break;}
					else break;
				}
			}
			else if (map[x][y] == '<') {
				for (int i=1;i<=y;i++) {
					if (map[x][y-i] == '.' || map[x][y-i] == '-') continue;
					else if (map[x][y-i] == '*') {map[x][y-i] = '.'; break;}
					else break;
				}
			}
			else if (map[x][y] == '>') {
				for (int i=1;i<W-y;i++) {
					if (map[x][y+i] == '.' || map[x][y+i] == '-') continue;
					else if (map[x][y+i] == '*') {map[x][y+i] = '.'; break;}
					else break;
				}
			}
		}
	}
}