import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] score = new int[n];
        for (int i = 0; i < n; i++) {
            score[i] = Integer.parseInt(br.readLine());
        }
        // 정렬
        Arrays.sort(score);
        int maxVal = 0;
        // 가장 적은 곳에 많은 점수 줌. 즉 최대 값을 만듬
        for (int i = 0; i < n; i++) {
            score[i] = score[i] + n - i;
            maxVal = Math.max(maxVal, score[i]);
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (score[i] + i >= maxVal) {
                ans++;
            }
        }
        System.out.println(ans);
    }
}