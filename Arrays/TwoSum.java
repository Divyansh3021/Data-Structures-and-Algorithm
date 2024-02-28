//-------------Problem: 1---------------

import java.util.*;

class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashMap = new HashMap<>();

        for (int index = 0; index < nums.length; index++) {
            int value = nums[index];
            int complement = target - value;

            if (hashMap.containsKey(complement)) {
                return new int[]{hashMap.get(complement), index};
            }

            hashMap.put(value, index);
        }

        return new int[0]; 
    };
}
