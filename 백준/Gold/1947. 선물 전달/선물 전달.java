import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        int DIV = 1_000_000_000;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] dp = new long[n+1];
        for (int i=0; i<=Math.min(n,3); i++) {
            dp[i] = i-1;
        }
        for (int i=4; i<=n; i++) {
            dp[i] = ((i-1)*(dp[i-1]+dp[i-2]))%DIV;
        }
        System.out.println(dp[n]);
    }
}