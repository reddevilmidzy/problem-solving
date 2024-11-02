import java.io.*;
import java.util.*;

public class Main {

    public static void main(final String[] args) throws IOException {

        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        final int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        final int[] nums = new int[n];
        final boolean[] used = new boolean[100_001];
        
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int one = 0;
        int two = 1;
        long res = 1;
        used[nums[one]] = true;
        while (two < n) {
            if (!used[nums[two]]) {
                used[nums[two]] = true;
                two += 1;                
                res += two - one;
            } else {
                used[nums[one]] = false;
                one += 1;
            }
        }
        System.out.print(res);
    }
}