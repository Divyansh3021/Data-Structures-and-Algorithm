//-------------Problem: 121--------------

class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int maxP = 0;
        int profit;
        while(r < prices.length){
            if(prices[l] < prices[r]){
                profit = prices[r] - prices[l];
                maxP = Math.max(maxP, profit);
            }
            else{
                l = r;
            }
            r += 1;
        }

        return maxP;
    }
}