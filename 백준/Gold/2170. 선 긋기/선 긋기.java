import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[][] arr = new int[n][2];
        int x;
        int y;
        long result = 0;
        for (int i=0; i< n; i++) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            arr[i][0] = x;
            arr[i][1] = y;
        }
        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if(o1[0] == o2[0]) {
                    return o1[1] - o2[1];
                } else {
                    return o1[0] - o2[0];
                }
            }
        });
        int nx = arr[0][0];
        int ny = arr[0][1];
        for(int i=0; i<n; i++) {
            x = arr[i][0];
            y = arr[i][1];
            if (ny < x) {
                result += ny - nx;
                nx = x;
                ny = y;
                continue;
            }
            ny = Math.max(ny, y);
        }
        result += ny - nx;
        System.out.println(result);
    }
}