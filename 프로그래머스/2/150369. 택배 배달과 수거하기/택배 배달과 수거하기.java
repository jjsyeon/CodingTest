class Solution {
    static int [] deliver, pickup;
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        deliver = deliveries.clone(); pickup = pickups.clone();
        long answer = 0;
        int maxD = -1, maxP = -1;
        for (int i = n-1; i > -1; i--){
            if (maxD == -1 && deliveries[i] > 0) maxD = i;
            if (maxP == -1 && pickups[i] > 0) maxP = i;
        }
        int dst;
        
        while (maxD > -1 || maxP > -1){
            dst = Math.max(maxD, maxP);
            answer += (dst+1) * 2;
            if (maxD > -1)
                maxD = update(cap, maxD, 1);
            if (maxP > -1)
                maxP = update(cap, maxP, 0);
        }
        
        
        return answer;
    }
    
    static int update(int amt, int maxD, int type){
        if (type == 1){
            while (maxD>-1) {
                if (deliver[maxD] > amt) {
                    deliver[maxD] -= amt;
                    amt = 0;
                    break;
                }
                else if (deliver[maxD] <= 0) {
                    maxD--;
                }
                else {
                    amt -= deliver[maxD];
                    deliver[maxD] = 0;
                    maxD--;
                }
            }
        }
        else {
            while (maxD >-1) {
                if (pickup[maxD] > amt) {
                    pickup[maxD] -= amt;
                    amt = 0;
                    break;
                }
                else if (pickup[maxD] <= 0) {
                    maxD--;
                }
                else {
                    amt -= pickup[maxD];
                    pickup[maxD] = 0;
                    maxD--;
                }
            }
        }
        return maxD;
    }
}