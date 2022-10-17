import java.util.*;
import java.io.*;
public class Main {
    static void init(long[] a, long[] tree, int node, int start, int end) {
        if (start == end) {
            tree[node] = a[start];
        } else {
            init(a, tree, node*2, start, (start+end)/2);
            init(a, tree, node*2+1, (start+end)/2+1, end);
            tree[node] = tree[node*2] + tree[node*2+1];
        }
    }
    // 업데이트
    static void update_lazy(long[] tree, long[] lazy, int node, int start, int end) {
        if (lazy[node] != 0) {
            tree[node] += (end-start+1)*lazy[node];
            if (start != end) {
                lazy[node*2] += lazy[node];
                lazy[node*2+1] += lazy[node];
            }
            lazy[node] = 0;
        }
    }
    static long query(long[] tree, long[] lazy, int node, int start, int end, int left, int right) {
        update_lazy(tree, lazy, node, start, end);
        if (left > end || right < start) {
            return 0;
        }
        if (left <= start && end <= right) {
            return tree[node];
        }
        long lsum = query(tree, lazy, node*2, start, (start+end)/2, left, right);
        long rsum = query(tree, lazy, node*2+1, (start+end)/2+1, end, left, right);
        return lsum+rsum;
    }
    static void update_range(long[] tree, long[] lazy, int node, int start, int end, int left, int right, long diff) {
        update_lazy(tree, lazy, node, start, end);
        if (left > end || right < start) {
            return;
        }
        if (left <= start && end <= right) {
            tree[node] += (end-start+1)*diff;
            if (start != end) {
                lazy[node*2] += diff;
                lazy[node*2+1] += diff;
            }
            return;
        }
        update_range(tree, lazy, node*2, start, (start+end)/2, left, right, diff);
        update_range(tree, lazy, node*2+1, (start+end)/2+1, end, left, right, diff);
        tree[node] = tree[node*2] + tree[node*2+1];
    }
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] line = br.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int m = Integer.parseInt(line[1]);
        int k = Integer.parseInt(line[2]);
        m += k;
        long[] a = new long[n];
        for (int i=0; i<n; i++) {
            a[i] = Long.parseLong(br.readLine());
        }
        int h = (int)Math.ceil(Math.log(n) / Math.log(2));
        int tree_size = (1 << (h+1));
        long[] tree = new long[tree_size];
        long[] lazy = new long[tree_size];
        init(a, tree, 1, 0, n-1);
        while (m-- > 0) {
            line = br.readLine().split(" ");
            int what = Integer.parseInt(line[0]);
            if (what == 1) {
                int left = Integer.parseInt(line[1]);
                int right = Integer.parseInt(line[2]);
                long diff = Long.parseLong(line[3]);
                update_range(tree, lazy, 1, 0, n-1, left-1, right-1, diff);
            } else {
                int left = Integer.parseInt(line[1]);
                int right = Integer.parseInt(line[2]);
                bw.write(query(tree, lazy, 1, 0, n-1, left-1, right-1)+"\n");
            }
        }
        bw.flush();
    }
}