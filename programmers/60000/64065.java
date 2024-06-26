import java.util.*;

class Solution {
    public int[] solution(String s) {
        String parsed = s.substring(2, s.length() - 2).replaceAll("\\},\\{", "-").replaceAll(",", "-");
        String[] tuples = parsed.split("-");
        HashMap<String, Integer> tupleMap = new HashMap<>();
        
        for(int i = 0; i < tuples.length; i++){
            tupleMap.put(tuples[i], tupleMap.getOrDefault(tuples[i], 0) + 1);
        }
        
        List<String> sorted = new ArrayList<>(tupleMap.keySet());
        sorted.sort((char1, char2) -> tupleMap.get(char2) - tupleMap.get(char1));
        int[] answer = new int[sorted.size()];
        
        for(int i = 0; i < sorted.size(); i++){
            answer[i] = Integer.parseInt(sorted.get(i));
        }
        
        return answer;
    }
}