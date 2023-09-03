import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st = br.readLine();
        int res = 0;

        String[] strings = st.split(" ");
        for (String string : strings) {
            if (Integer.parseInt(string) > 0) {
                res++;
            }
        }
        System.out.println(res);
    }
}