import java.util.*;

class Solution {
    private static final int ASCII_A = 65;
    private static final int NUM_ALPHABET = 26;
    
    public int[] solution(String msg) {
        List<Integer> answer = new ArrayList<>();
        Map<String, Integer> dictionary = new HashMap<>();
        StringBuilder origin = new StringBuilder(msg);
        String before = "";
        String temp = "";
        
        int head = 0;
        int rear = 1;
        
        for(int i = ASCII_A; i < ASCII_A + NUM_ALPHABET; i++){
            dictionary.put((char)i + "", dictionary.size() + 1);
        }
        
        while(head < msg.length() && rear <= msg.length()){
            // 1. head ~ rear에 해당하는 글자가 있는지 확인
            // 1-1) 있는 경우 - rear + 1까지의 글자가 있는지 확인
            // 1-2) 없는 경우 - head ~ rear 글자를 dictionary에 등록 & answer에 추가
            // 2. head = rear, rear = head + 1로 치환
            temp = origin.substring(head, rear);
            
            if(dictionary.containsKey(temp)){
                if(rear == msg.length()){
                    answer.add(dictionary.get(temp));
                    break;
                }
                
                rear++;
                before = temp;
                continue;
            }
            
            dictionary.put(temp, dictionary.size() + 1);
            answer.add(dictionary.get(before));
            head = rear - 1;
            rear = head + 1;
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}