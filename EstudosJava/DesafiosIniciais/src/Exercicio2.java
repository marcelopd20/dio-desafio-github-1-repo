import java.io.IOException;
import java.util.Scanner;

public class Exercicio2 {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        for (int i = 1; i <= n; ++i){
            if (i % 2 == 0){
                System.out.println(i);
            }
        }
    }
}
