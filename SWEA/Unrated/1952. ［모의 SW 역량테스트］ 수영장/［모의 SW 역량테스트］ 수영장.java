import java.util.*;
import java.io.*;

public class Solution {
	
	public static void main(String [] args) throws Exception {
		BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		int [] tickets = new int [4];
		int [][] plans = new int [15][3];
		for (int t = 1; t <= T; t++) {
			st = new StringTokenizer(br.readLine());
			for (int i = 0 ; i < 4; i++) tickets[i] = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			for (int m = 1 ; m <= 12; m++) plans[m][0] = Integer.parseInt(st.nextToken());
			
			for (int m = 1 ; m < 15 ; m++) {
				plans[m][0] = plans[m][0] * tickets[0] < tickets[1] ? plans[m][0] * tickets[0] : tickets[1];
				plans[m][1] = plans[m-1][1] + plans[m][0];
				if (m >= 3) { 
					plans[m][2] = plans[m-3][1] + tickets[2]; 
					plans[m][1] =Math.min(plans[m][2], plans[m][1]);
				}
			}
			
			sb.append("#").append(t).append(" ").append(plans[14][1] < tickets[3] ? plans[14][1] : tickets[3]).append("\n");
		}
		System.out.println(sb);
	}
}
