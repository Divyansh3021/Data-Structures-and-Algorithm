//---------------Problem: 22---------------

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        StringBuilder stack = new StringBuilder();

        generateParenthesisUtil(n, 0, 0, stack, res);

        return res;
    }

    private void generateParenthesisUtil(int n, int open, int close, StringBuilder stack, List<String> res) {
        if (open == close && close == n) {
            res.add(stack.toString());
            return;
        }

        if (open < n) {
            stack.append("(");
            generateParenthesisUtil(n, open + 1, close, stack, res);
            stack.deleteCharAt(stack.length() - 1);
        }

        if (close < open) {
            stack.append(")");
            generateParenthesisUtil(n, open, close + 1, stack, res);
            stack.deleteCharAt(stack.length() - 1);
        }
    }
}
