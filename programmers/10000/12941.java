import java.util.Arrays;
class Solution
{
    public int solution(int []A, int []B)
    {
        Arrays.sort(A);
        Arrays.sort(B);
        
        int endIndex = A.length - 1;
        int answer = 0;
        
        for(int i = 0; i <= endIndex; i++){
            answer += A[i] * B[endIndex - i];
        }
        
        return answer;
    }
}