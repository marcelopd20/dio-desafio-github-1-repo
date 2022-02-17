package Exercicios.arrays;

/**
 * Crie um vetor de 6 números inteiros e mostre-os na ordem inversa.
 */
public class Exercicio1_OrdemInversa {

    public static void main(String[] args) {

        int[] vetor = {5, 66, -1, 26, 1, 0};

        int count = 0;
        System.out.print("Vetor: ");
        while (count < (vetor.length)) {
            System.out.print(vetor[count] + " ");
            ++count;
        }
        System.out.println();
        System.out.print("Vetor inverso: ");
        for (int i = (vetor.length - 1); i >= 0; i--){
            System.out.print(vetor[i] + " ");
        }
    }
}
