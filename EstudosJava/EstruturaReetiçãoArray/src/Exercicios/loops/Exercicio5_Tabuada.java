package Exercicios.loops;

import java.util.Scanner;

/**
 * Desenvolva um geador de tabuada,capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10
 * O usufário deve informar qual numero ele deseja ver a tabuada
 * A saida deve ser a tabuada.
 */
public class Exercicio5_Tabuada {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Tabuada: ");
        int tabuada = scan.nextInt();

        System.out.println("Tabuada do "+ tabuada +"!");
        for(int i = 1;i <= 10;i++) {
            System.out.println(i + " * " + tabuada + " = " + (tabuada*i));
        }


    }

}
