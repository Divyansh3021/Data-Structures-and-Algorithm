//----------------Problem: 338-----------------

class CountingBits {
    public int[] countBits(int n) {
        int ans[] = new int[n+1];
        ans[0] = 0;
        int offset = 1;

        for(int i = 1; i < n+1; i++){
            if(i == offset*2){
                offset = i;
            }
            ans[i] = 1 + ans[i-offset];
        }

        return ans;
    }
}