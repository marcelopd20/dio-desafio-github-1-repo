import java.util.Scanner;

public class Exercicio1 {

        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            double a, b, media;

            a = sc.nextDouble();
            b = sc.nextDouble();

            //TODO: Complete os espaços em branco com as respectivas variáveis para o cálculo da média.
            media = ((a* 3.5) + (b* 7.5))/11;

            //TODO: Complete com a variável que representa o resultado da média.
            System.out.printf("MEDIA = %.5f", media);
            System.out.println();
        }
    }
