import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int hambuger = 2001;
        int drink = 2001;
        for(int i=0; i<3; i++) {
            int newHambuger = Integer.parseInt(br.readLine());
            hambuger = Math.min(hambuger, newHambuger);
        }

        for(int i=0; i<2; i++) {
            int newDrink = Integer.parseInt(br.readLine());
            drink = Math.min(drink, newDrink);
        }
        System.out.println(hambuger+drink-50);
    }
}