//-------------Problem: 1470--------------

class ShuffleTheArray {
    public int[] shuffle(int[] nums, int n) {
        for(int i = 0; i < n; i++){
            nums[i] = nums[i] << 10;
            nums[i] = nums[i] | nums[i+n];
        }

        int j = 2 * n - 1;
        int x, y;
        for(int i = n-1; i > -1; i--){
            y = nums[i] & (int)(Math.pow(2, 10) - 1);
            x = nums[i] >> 10;
            nums[j] = y;
            nums[j-1] = x;
            j -= 2;
        }
        return nums;
    }
}