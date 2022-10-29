import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        
        Solution solution = new Solution();
        System.out.println(solution.solution(n));
    }
}

class Solution {
    public int solution(int number) {
        int crap = 0;
        for (int i=1; i<=number; i++){
            int nowNumber = i;
            while (nowNumber > 0){
                if (nowNumber % 10 ==3){
                    crap ++;
                    nowNumber /= 10;
                    continue;
                }
                if (nowNumber % 10 == 6){
                    crap ++;
                    nowNumber /= 10;
                    continue;
                }
                if (nowNumber % 10 == 9){
                    crap ++;
                    nowNumber /= 10;
                    continue;
                }
                nowNumber /= 10;
            }
        }
        return crap;
    }
}
