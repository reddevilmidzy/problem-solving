import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int n = Integer.parseInt(br.readLine());
        final StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        boolean[] dp = new boolean[7];
        dp[0] = true;

        for (int num : nums) {
            boolean[] next = new boolean[7];
            for (int i = 0; i < 7; i++) {
                if (dp[i]) {
                    next[i] = true;
                    next[(num + i) % 7] = true;
                }
            }
            if (next[4]) {
                System.out.print("YES");
                return;
            }
            dp = next;
        }
        System.out.print("NO");
    }
}