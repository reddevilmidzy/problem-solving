import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            if (n == 0 && m == 0) {
                break;
            }
            int[] arr = new int[n];
            long[][] dp = new long[n][m];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
                dp[i][0] = 1;
            }

            for (int i = 0; i < n; i++) {
                for (int j = i - 1; j >= 0; j--) {
                    if (arr[i] > arr[j]) {
                        for (int k = 0; k < m-1; k++) {
                            dp[i][k+1] += dp[j][k];
                        }
                    }
                }
            }
            long ans = 0L;
            for (int i = 0; i < n; i++) {
                ans += dp[i][m-1];
            }
            System.out.println(ans);
        }
    }
}