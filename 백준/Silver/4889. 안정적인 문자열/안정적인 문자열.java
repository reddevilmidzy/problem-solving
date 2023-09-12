import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int idx = 0;
        while (true) {
            idx++;
            StringTokenizer st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            if (str.contains("-")) {
                break;
            }
            int stk = 0;
            int tmp = 0;

            for (int i = 0; i < str.length(); i++) {

                if (str.charAt(i) == '{') {
                    stk++;
                } else if (stk > 0) {
                    stk--;
                } else {
                    tmp++;
                }
            }
            sb.append(idx+". " + Math.round(Math.ceil(stk/2.0) + Math.ceil(tmp/2.0)) + "\n");
        }
        System.out.print(sb);
    }
}
