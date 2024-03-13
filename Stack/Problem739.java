//---------------Problem: 739------------------

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        Deque<int[]> stack = new ArrayDeque<>();

        for (int i = 0; i < temperatures.length; i++) {
            int t = temperatures[i];
            while (!stack.isEmpty() && t > stack.peek()[0]) {
                int[] stackTop = stack.pop();
                res[stackTop[1]] = i - stackTop[1];
            }
            stack.push(new int[]{t, i});
        }
        return res;
    }
}
