import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(final String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final StringBuilder sb = new StringBuilder();
        final int n = Integer.parseInt(br.readLine());

        final int[][] points = new int[n][3];

        for (int i = 0; i < n; i++) {
            final StringTokenizer st = new StringTokenizer(br.readLine());
            points[i][0] = Integer.parseInt(st.nextToken());
            points[i][1] = Integer.parseInt(st.nextToken());
            points[i][2] = Integer.parseInt(st.nextToken());
        }

        final int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            final StringTokenizer st = new StringTokenizer(br.readLine());
            final long x = Long.parseLong(st.nextToken());
            final long y = Long.parseLong(st.nextToken());
            final long z = Long.parseLong(st.nextToken());
            final long r = Long.parseLong(st.nextToken());

            int cnt = 0;
            for (final int[] point : points) {
                if ((x - point[0]) * (x - point[0]) + (y - point[1]) * (y - point[1]) + (z - point[2]) * (z - point[2])
                    <= r * r) {
                    cnt += 1;
                }
            }
            sb.append(cnt).append("\n");
        }
        System.out.print(sb);
    }
}
