//---------------------Problem: 875--------------------------

import java.util.Arrays;
import java.util.List;

class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        int left = 1;
        int right = piles[piles.length - 1];
        int result = piles[piles.length - 1];

        while (left <= right) {
            int mid = left + (right - left) / 2;

            int hours = 0;
            for (int i : piles) {
                hours += Math.ceil((double) i / mid);
            }

            if (hours <= h) {
                result = Math.min(result, mid);
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return result;
    }
}
