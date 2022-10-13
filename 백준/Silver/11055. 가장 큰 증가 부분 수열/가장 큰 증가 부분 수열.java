import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        int[] dp = new int[n];
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            a[i] = dp[i] = Integer.parseInt(tokenizer.nextToken());
        }

        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                if(a[i]>a[j]){
                    dp[i] = Math.max(dp[i], dp[j]+a[i]);
                }
            }
        }
        int res = 0;
        for (int i=0;i<n;i++){
            if (dp[i]>res){
                res = dp[i];
            }
        }
        System.out.println(res);

    }
}
