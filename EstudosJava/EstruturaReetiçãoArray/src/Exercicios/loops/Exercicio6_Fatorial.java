package Exercicios.loops;

import java.util.Scanner;

/**
 * Faça um programa quie calcule o fatorial de um número inteiro fornecido pelo usuário.
 * Ex: 5! = 120
 */
public class Exercicio6_Fatorial {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int fatorial;
        System.out.println("Fatorial de: ");
        fatorial = scan.nextInt();

        int multiplicacao = 1;

        for (int i = fatorial; i >= 1; i--){
            multiplicacao *= i;
        }

        System.out.println(fatorial +"!: " + multiplicacao);
    }
}
