import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        int[][] dp = new int[n+1][n+1];
        for(int i=0; i<=n; i++) {
            for(int j=0; j<=n; j++) {
                dp[i][j] = -1;
            }
            dp[i][0] = 1;
            dp[i][1] = i;
        }
        int result = solution(dp, n, k);
        System.out.println(result);
    }


    public static int solution(int[][] dp, int n, int k) {
        int DIV = 1_000_000_003;
        if (k>(n/2)) {
            dp[n][k] = 0;
            return 0;
        }
        if (dp[n][k] != -1) {
            return dp[n][k];
        }
        dp[n][k] = (solution(dp, n-1, k)%DIV) + (solution(dp, n-2, k-1)%DIV);
        return dp[n][k]%DIV;
    }
}