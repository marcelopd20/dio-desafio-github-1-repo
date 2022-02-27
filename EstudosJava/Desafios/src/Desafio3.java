import java.io.IOException;
import java.util.Scanner;

public class Desafio3 {
    public static void main(String[] args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        Double numero = leitor.nextDouble();
        System.out.println(String.format((String.valueOf(numero).startsWith("-") ? "" : "+") + "%.4E", numero));


    }
}
