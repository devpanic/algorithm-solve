import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int head = 0;
        int totalPeople = people.length;
        Arrays.sort(people);
        
        for(int i = totalPeople - 1; i >= head; i--){
            if(people[i] + people[head] <= limit){
                head++;
            }
            answer++;
        }
        
        return answer;
    }
}