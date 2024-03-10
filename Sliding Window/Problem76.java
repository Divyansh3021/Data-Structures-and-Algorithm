//-----------------Problem: 76-------------------

import java.util.HashMap;

class Solution {
    public String minWindow(String s, String t) {
        if (t.equals("")) return "";

        HashMap<Character, Integer> countT = new HashMap<>();
        HashMap<Character, Integer> window = new HashMap<>();
        for (char c : t.toCharArray()) {
            countT.put(c, 1 + countT.getOrDefault(c, 0));
        }

        int have = 0;
        int need = countT.size();
        int[] res = new int[]{-1, -1};
        int reslen = Integer.MAX_VALUE;
        int l = 0;

        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            window.put(c, 1 + window.getOrDefault(c, 0));

            if (countT.containsKey(c) && window.get(c).equals(countT.get(c))) {
                have++;
            }

            while (have == need) {
                if ((r - l + 1) < reslen) {
                    res[0] = l;
                    res[1] = r;
                    reslen = r - l + 1;
                }

                window.put(s.charAt(l), window.get(s.charAt(l)) - 1);
                if (countT.containsKey(s.charAt(l)) && window.get(s.charAt(l)) < countT.get(s.charAt(l))) {
                    have--;
                }
                l++;
            }
        }
        int left = res[0];
        int right = res[1];
        return reslen != Integer.MAX_VALUE ? s.substring(left, right + 1) : "";
    }
}
