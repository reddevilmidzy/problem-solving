import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] graph = new int[n + 1][n + 1];
        int[][] dp = new int[m][n + 1];

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            if (u < v) {
                graph[u][v] = Math.max(graph[u][v], w);
            }
        }

        for (int i = 1; i <= n; i++) {
            dp[1][i] = Math.max(dp[1][i], graph[1][i]);
        }

        for (int i = 1; i < m - 1; i++) {
            for (int cur = 1; cur <= n; cur++) {
                if (dp[i][cur] == 0) continue;
                for (int nxt = 1; nxt <= n; nxt++) {
                    if (cur > nxt || graph[cur][nxt] == 0) continue;
                    dp[i+1][nxt] = Math.max(dp[i+1][nxt], dp[i][cur]+graph[cur][nxt]);
                }
            }
        }

        int res = 0;
        for (int i = 0; i < m; i++) {
            res = Math.max(res, dp[i][n]);
        }
        System.out.println(res);
    }
}
