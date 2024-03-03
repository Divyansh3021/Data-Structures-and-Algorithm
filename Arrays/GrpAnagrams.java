//---------------Problem: 49----------------

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GrpAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagMap = new HashMap<>();
        
        for (String word : strs) {
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sortedWord = new String(charArray);

            if (anagMap.containsKey(sortedWord)) {
                anagMap.get(sortedWord).add(word);
            } else {
                List<String> anagrams = new ArrayList<>();
                anagrams.add(word);
                anagMap.put(sortedWord, anagrams);
            }
        }

        return new ArrayList<>(anagMap.values());
    }
}
