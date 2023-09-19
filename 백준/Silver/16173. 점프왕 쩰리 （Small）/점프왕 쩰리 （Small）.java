import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[][] board = new int[n][n];

        int[] dy = new int[]{1,0};
        int[] dx = new int[]{0,1};

        Queue<Integer[]> queue = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j<n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        boolean[][] visited = new boolean[n][n];

        visited[0][0] = true;
        queue.add(new Integer[]{0,0});
        Integer[] pos;

        while (!queue.isEmpty()) {
            pos = queue.poll();
            if (Arrays.equals(pos, new Integer[]{n - 1, n - 1})) {
                System.out.println("HaruHaru");
                return;
            }

            for (int i=0; i<2; i++) {
                int ny = pos[0] + dy[i] * board[pos[0]][pos[1]];
                int nx = pos[1] + dx[i]  * board[pos[0]][pos[1]];
                if (ny < 0 || nx < 0 || ny >= n || nx >= n) {
                    continue;
                }

                if (!visited[ny][nx]) {
                    visited[ny][nx] = true;
                    queue.offer(new Integer[]{ny,nx});
                }
            }
        }
        System.out.println("Hing");
    }
}
