import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        String[][] board = new String[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            System.arraycopy(st.nextToken().split(""), 0, board[i], 0, n);
        }

        int row = 0;
        int col = 0;

        for (int i = 0; i < n; i++) {
            int tmpCol = 0;
            int tmpRow = 0;
            for (int j = 0; j < n; j++) {
                if (board[i][j].equals(".")) {
                    tmpCol++;
                }
                if (board[i][j].equals("X")) {
                    if (tmpCol > 1) {
                        col++;
                    }
                    tmpCol = 0;
                }

                if (board[j][i].equals(".")) {
                    tmpRow++;
                }
                if (board[j][i].equals("X")) {
                    if (tmpRow > 1) {
                        row++;
                    }
                    tmpRow = 0;
                }
            }
            if (tmpCol > 1) {
                col++;
            }
            if (tmpRow > 1) {
                row++;
            }
        }
        System.out.print(col + " " + row);
    }
}