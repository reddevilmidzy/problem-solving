import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int left = 0;
        int right = n-1;
        long leftAns = 2000000000l;
        long rightAns = 2000000000l;
        long shake = leftAns + rightAns;
        while (left < right) {
            long tmp = arr[left] + arr[right];
            if (Math.abs(tmp) < shake) {
                shake = Math.abs(tmp);
                leftAns = arr[left];
                rightAns = arr[right];
            }
            if (tmp < 0) {
                left += 1;
            } else if (tmp > 0) {
                right -= 1;
            } else {
                leftAns = arr[left];
                rightAns = arr[right];
                break;
            }
        }
        System.out.println(leftAns + " " + rightAns);
    }
}