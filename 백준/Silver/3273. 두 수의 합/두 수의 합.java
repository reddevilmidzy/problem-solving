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
        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        int x = Integer.parseInt(br.readLine());

        int left = 0;
        int right = n-1;
        int ans = 0;
        while (left < right && right < n) {
            if (arr[left] + arr[right] == x) {
                ans++;
                right--;
            } else if (arr[left] + arr[right] < x) {
                left++;
            } else {
                right--;
            }
        }

        System.out.println(ans);
    }
}