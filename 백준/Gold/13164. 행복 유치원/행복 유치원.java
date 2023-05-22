import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args)throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine().trim());
        int n = Integer.parseInt(s.nextToken());
        int k = Integer.parseInt(s.nextToken());

        int[] nums = new int[n];
        int res = 0;
        Integer[] diff = new Integer[n-1];
        s = new StringTokenizer(br.readLine().trim());
        for (int i=0;i<n;i++){
            nums[i] = Integer.parseInt(s.nextToken());
        }
        for (int j=0;j<n-1;j++){
            diff[j] = nums[j+1]-nums[j];
        }
        Arrays.sort(diff, Collections.reverseOrder());

        for (int i=k-1;i<diff.length;i++){
            res += diff[i];
        }
        System.out.println(res);
    }
}