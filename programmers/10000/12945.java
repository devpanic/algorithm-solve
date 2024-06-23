import java.math.BigInteger;

class Solution {
    public BigInteger solution(int n) {
        BigInteger[] input = new BigInteger[n + 1];
        input[0] = BigInteger.ZERO;
        input[1] = BigInteger.ONE;
        
        for (int i = 2; i <= n; i++) {
            input[i] = input[i - 1].add(input[i - 2]);
        }

        return input[n].mod(BigInteger.valueOf(1234567));
    }
}