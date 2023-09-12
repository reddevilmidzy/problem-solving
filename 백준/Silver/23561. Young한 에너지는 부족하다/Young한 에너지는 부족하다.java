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
        String[] stringArr = br.readLine().split(" ");
        int[] intArr = new int[3*n];

        for (int i = 0; i < 3*n; i++) {
            intArr[i] = Integer.parseInt(stringArr[i]);
        }

        Arrays.sort(intArr);
        System.out.println(intArr[3*n-n-1] - intArr[n]);
    }
}
