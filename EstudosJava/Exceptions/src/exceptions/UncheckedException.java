package exceptions;

import javax.swing.*;

public class UncheckedException {
    public static void main(String[] args) {

        boolean continueLooping = true;

        do {
            String a = JOptionPane.showInputDialog("Numerador: ");
            String b = JOptionPane.showInputDialog("Denominador: ");
            try {

                double resultado = dividir(Integer.parseInt(a), Integer.parseInt(b));
                System.out.println("Resultado: " + resultado);
                continueLooping = false;

            } catch (NumberFormatException e) {

                //e.printStackTrace();
                JOptionPane.showMessageDialog(null, "Entrada inválida, informe um número inteiro" + e.getMessage());

            } catch (ArithmeticException e) {

                JOptionPane.showMessageDialog(null, "Impossível dividir por zero.");

            } finally {

                System.out.println("Chegou no finally!");

            }

        }while (continueLooping);

        System.out.println("O código continua...");

    }

    public static double dividir(double a, double b){ return a/b;}
}
