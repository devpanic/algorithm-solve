class Solution {
    // 주어진 자연수를 연속된 자연수의 합으로 표현하는 방법의 수는 주어진 수의 홀수 약수의 개수와 같다
    public int solution(int n) {
        int max = (n % 2 == 0) ? (n / 2) : (n / 2 + 1);
        int answer = 0;
        int sum = 0;
        int curr = 0;
        
        if(n == 1) return 1;
        
        for(int i = 1; i <= max; i++){
            curr = i;
            while(sum < n){
                sum += curr;
                curr++;
            }        
            if(sum == n){
                answer++;
            }
            sum = 0;
        }
        
        return answer + 1;
    }
}