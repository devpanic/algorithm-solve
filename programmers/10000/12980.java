import java.util.*;

public class Solution {
    public int solution(int n) {
        int ans = 0;

        while(n > 1){
            if(n % 2 == 0){
                n /= 2;
                continue;
            }
            
            n -= 1;
            n /= 2;
            ans++;
        }

        return ans + 1;
    }
}