package Exercicios.loops;

import java.util.Scanner;

/**Faça um programa que peça N números inteiros,
 * calcule e mostre a quantidade de números pares
 *e a quantidade de números impares.
 */
public class Exercicio4_ParImpar {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int quantNumeros;
        System.out.println("Quantos números: ");
        quantNumeros = scan.nextInt();

        int count = 0;
        int numero;
        int quantPar = 0;
        int quantImpar = 0;

        do {
            System.out.println("Número: ");
            numero = scan.nextInt();
            if (numero % 2 == 0) ++quantPar;
            else ++quantImpar;

            ++count;

        } while(count < quantNumeros);

        System.out.println("Quantidade de pares: " + quantPar);
        System.out.println("Quantidade de impares: " + quantImpar);

    }
}
