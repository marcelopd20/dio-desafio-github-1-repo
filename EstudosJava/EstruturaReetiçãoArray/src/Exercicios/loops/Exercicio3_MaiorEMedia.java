package Exercicios.loops;

import java.util.Scanner;

/**
 * Faça um programa que leia 5 números
 * e informe o maior número
 * e a média desses números.
 */
public class Exercicio3_MaiorEMedia {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int numero;
        int count = 0;
        int maior = 0;
        int soma = 0;

        do {
            System.out.println("Número: ");
            numero = scan.nextInt();
            if (count == 0) maior = numero;
            else if(numero > maior) maior = numero;
            soma += numero;
            ++count;
        } while(count < 5);
        System.out.println("Maior número: " + maior);
        System.out.println("Soma dos números: " + soma);
        System.out.println("Média: " + (soma/5));
    }
}
