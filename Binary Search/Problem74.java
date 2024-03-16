//-------------------Problem: 74--------------------------

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int[] end_int = new int[matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            end_int[i] = matrix[i][matrix[i].length - 1];
        }

        int left = 0;
        int right = end_int.length - 1;
        int mid;
        if(end_int[right] < target){
            return false;
        }

        while(left <= right){
            mid = (left + right)/2;

            if(end_int[mid] > target){
                right = mid - 1;
            }
            else if (end_int[mid] < target){
                left = mid + 1;
            }
            else{
                return true;
            }
        }

        int subarray = left;
        left = 0;
        right = matrix[subarray].length - 1;

        while(left <= right){
            mid = (left + right)/2;

            if(matrix[subarray][mid] > target){
                right = mid - 1;
            }
            else if (matrix[subarray][mid] < target){
                left = mid + 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
}