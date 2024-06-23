import java.lang.Math;

class Solution {
    public int[] solution(int brown, int yellow) {
        // (갈색 격자 수 + 노란 격자 수) 약수 모음과 (갈색 격자 수 약수 - 1) 모음이 노란 격자 수와 맞으면 정답
        // (갈색격자 약수 - 2) * (짝 약수 - 2) = 노란 격자 수
        int total = brown + yellow;
        int standard = (int)(Math.sqrt(total)) + 1;
        int div = 0;
        int[] answer = {0, 0};
        
        for(int i = 3; i < standard; i++){
            if(total % i == 0){
                div = (total / i);
                if((i - 2) * (div - 2) == yellow){
                    if(div >= i){
                        answer[0] = div;
                        answer[1] = i;
                        break;
                    }
                    
                    answer[0] = i;
                    answer[1] = div;
                    break;
                }
            }
        }
        
        return answer;
    }
}