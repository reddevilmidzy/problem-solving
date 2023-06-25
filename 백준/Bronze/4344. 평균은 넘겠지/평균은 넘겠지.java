import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        for (int i = 0; i < c; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int[] nums = new int[n];
            int tot = 0;
            for (int j = 0; j < n; j++) {
                nums[j] = Integer.parseInt(st.nextToken());
                tot += nums[j];
            }
            double avg = tot / n;

            int cnt = 0;
            for (int num : nums) {
                if (num > avg) {
                    cnt++;
                }
            }
            System.out.println(String.format("%.3f", (double) cnt / n * 100) + "%");
        }
    }
}
