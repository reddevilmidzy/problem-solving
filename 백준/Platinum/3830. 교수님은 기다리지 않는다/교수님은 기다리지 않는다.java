import java.io.*;
import java.util.*;

public class Main {

    private static int[] parent;
    private static long[] weight;

    public static void main(final String[] args) throws IOException {

        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            if (n == 0) {
                break;
            }
    
            parent = new int[n + 1];
            weight = new long[n + 1];

            for (int i = 1; i <= n; i++) {
                parent[i] = i;
                weight[i] = 0;
            }

            while (m-->0) {
                st = new StringTokenizer(br.readLine());
                String token = st.nextToken();

                if ("!".equals(token)) {
                    int a = Integer.parseInt(st.nextToken());
                    int b = Integer.parseInt(st.nextToken());
                    int w = Integer.parseInt(st.nextToken());
                    union(a, b, w);

                } else if ("?".equals(token)) {
                    int u = Integer.parseInt(st.nextToken());
                    int v = Integer.parseInt(st.nextToken());
                    if (find(u) != find(v)) {
                        sb.append("UNKNOWN").append("\n");
                    } else {
                        sb.append(weight[v] - weight[u]).append("\n");
                    }
                }
            }
        }
        System.out.print(sb);
    }


    private static int find(final int x) {
        if (parent[x] != x) {
            int y = find(parent[x]);
            weight[x] += weight[parent[x]];
            parent[x] = y;
        }
        return parent[x];
    }

    private static void union(final int a, final int b, final int w) {
        int pa = find(a);
        int pb = find(b);

        if (pa != pb) {
            weight[pb] = (-weight[b]) + weight[a] + w;
            parent[pb] = pa;
        }
    }
}
