import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());
        int[] nums = new int[3];

        for (int i = 1; i <= t; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < 3; j++) {
                nums[j] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(nums);

            System.out.println("Case #" + i + ": " + Solve(nums));
        }
    }


    static String Solve(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        if (set.size() == 1) {
            return "equilateral";
        } else if (set.size() == 2 && nums[0] + nums[1] > nums[2]) {
            return "isosceles";
        } else if (set.size() == 3 && nums[0] + nums[1] > nums[2]) {
            return "scalene";
        }
        return "invalid!";
    }
}