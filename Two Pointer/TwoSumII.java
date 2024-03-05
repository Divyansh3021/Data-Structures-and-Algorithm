//------------------Problem: 167------------------

class TwoSumII {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length - 1;
        int curr_sum;
        int[] res = new int[2];
        while(i<j){
            curr_sum = numbers[i] + numbers[j];

            if(curr_sum == target){
                res[0] = i+1;
                res[1] = j+1;
                return res;
            }
            else if(curr_sum < target){
                i += 1;
            }
            else{
                j -= 1;
            }
        }
        return res;
    }
}