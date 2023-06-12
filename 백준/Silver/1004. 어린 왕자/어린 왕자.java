import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        int x1,y1,x2,y2,n;
        int x,y,r,r1,r2;
        for (int i = 0; i < t; i++) {
            int ans = 0;
            st = new StringTokenizer(br.readLine());
            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());

            n = Integer.parseInt(br.readLine());
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                x = Integer.parseInt(st.nextToken());
                y = Integer.parseInt(st.nextToken());
                r = Integer.parseInt(st.nextToken());

                r = r*r;
                r1 = (x1 - x) * (x1 - x) + (y1 - y) * (y1 - y);
                r2 = (x2 - x) * (x2 - x) + (y2 - y) * (y2 - y);

                if ((r1 < r && r2 > r) || (r1 > r && r2 < r)) {
                    ans++;
                }
            }
            System.out.println(ans);
        }
    }
}
