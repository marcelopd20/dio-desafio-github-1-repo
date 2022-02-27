package Collections.List;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

/*
Utilizando listas, faça um programa que faça 5 perguntas para uma
pessoa sobre um crime. As perguntas são:
1. "Telefonou para a vítima?"
2. "Esteve no local do crime?"
3. "Mora perto da vítima?"
4. "Devia para a vítima?"
5. "Já trabalhou com a vítima?"

Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassina". Caso contrário, ela será classificado como "Inocente".
 */
public class Exercicio2List {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        List<String> perguntas = new ArrayList<>();
        int count = 0;

        System.out.print("Telefonou para a vítima? ");
        perguntas.add(scan.next().toUpperCase());
        System.out.print("Esteve no local do crime? ");
        perguntas.add(scan.next().toUpperCase());
        System.out.print("Mora perto da vítima? ");
        perguntas.add(scan.next().toUpperCase());
        System.out.print("Devia para a vítima? ");
        perguntas.add(scan.next().toUpperCase());
        System.out.print("Já trabalhou com a vítima? ");
        perguntas.add(scan.next().toUpperCase());
        for (String Pergunta : perguntas){
            if (Pergunta.equals("SIM")){
                count++;
            }
        }
        if (count == 5) System.out.println("Assassina");
        else if(count >= 3) System.out.println("Cúmplice");
        else if(count >= 2) System.out.println("Suspeita");
        else System.out.println("Inocente");
    }
}
