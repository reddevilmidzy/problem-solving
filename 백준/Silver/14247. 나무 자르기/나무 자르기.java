import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        String[] tmp = br.readLine().split(" ");

        long ans = 0L;

        for (int i = 0; i < n; i++) {
            ans += Integer.parseInt(tmp[i]);
        }

        int[] a = new int[n];
        tmp = br.readLine().split(" ");

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(tmp[i]);
        }
        Arrays.sort(a);

        for (int i = 0; i < n; i++) {
            ans += (long) a[i] * i;
        }

        System.out.println(ans);
    }
}