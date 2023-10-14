class Solution {

    private long MOD = 1000_000_007;

    public int countGoodNumbers(long n) {
        long even = (n+1)/2;
        long odd = n/2;
        long even_pow = pow(5, even)%MOD;
        long odd_pow = pow(4, odd)%MOD;

        return (int)((even_pow*odd_pow)%MOD);
    }

    private long pow(long x, long n){
        if (n==0) return 1;

        long temp = pow(x, n/2);

        if(n%2==0){
            return (temp*temp)%MOD;
        }
        else{
            return (x*temp*temp)%MOD;
        }
    }
}