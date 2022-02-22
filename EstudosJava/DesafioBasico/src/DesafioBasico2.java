import java.io.IOException;
import java.util.Scanner;

public class DesafioBasico2 {

    public static void main(String[] args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        double A = leitor.nextDouble();
        double B = leitor.nextDouble();
        double C;
        C = ((B-A) * 100)/ A;
        //Escreva aqui a sua lógica
        System.out.printf("%.2f", C);
        System.out.print("%");
    }

}