package Collections.List;

import java.util.*;

class ExemploList {
    public static void main(String[] args) {
        //dada uma lista com 7 notas de um aluno, faça:
        //List notas = new ArrayList(); //anterior ao java5
        //List<Double> notas = new ArrayList<>();
        //ArrayList<Double> notas = new ArrayList<>();
        //List<Double> notas = new ArrayList<>(Arrays.asList(7d, 8.5, 9.3, 5d, 8d, 3.6));
        /*List<Double> notas = Arrays.asList(7d, 8.5, 9.3, 5d, 8d, 3.6);
          notas.add(18d);
          System.out.println(notas);
         */
        /*List<Double> notas = List.of(7d, 8.5, 9.3, 5d, 8d, 3.6);
          notas.add(1d);
          notas.remove(5d);
          System.out.println(notas);
         */


        System.out.print("Crie uma lista e adicione as sete notas: ");

        List<Double> notas = new ArrayList<>();
        notas.add(7d);
        notas.add(8.5);
        notas.add(9.3);
        notas.add(5.0);
        notas.add(7.0);
        notas.add(0.0);
        notas.add(3.6);
        System.out.println(notas.toString());

        System.out.println("Exiba a posição da nota 5.0: " + notas.indexOf(5d));

        System.out.print("Adicione na lista a nota 8.0 na posição 4: ");
        notas.add(4, 8d);
        System.out.println(notas);

        System.out.print("Substitua a nota 5.0 pela nota 6.0: ");
        notas.set(notas.indexOf(5d), 6d);
        System.out.println(notas);

        System.out.println("Confira se na lista há o elemento 5: " + notas.contains(5d));

        System.out.print("Exiba todas as notas na ordem em que foram informados: ");
        for (Double nota : notas) System.out.print(nota + "   ");

        System.out.println();

        System.out.println("Exiba a terceira nota adicionado: " + notas.get(2));

        System.out.println("Exiba a menor nota: " + Collections.min(notas));

        System.out.println("Exiba a maior nota: " + Collections.max(notas));

        System.out.print("Exiba a soma das notas: " );
        Iterator<Double> iterator = notas.iterator();
        Double soma = 0d;
        while (iterator.hasNext()) {
            Double next = iterator.next();
            soma += next;
        }
        System.out.println(soma);

        System.out.printf("Exiba a média das notas: %.2f", (soma/notas.size()));
        System.out.println();

        System.out.print("Remova a nota 0.0: ");
        notas.remove(0d);
        System.out.println(notas);

        System.out.print("Remova a nota na posição 0: ");
        notas.remove(0);
        System.out.println(notas);

        System.out.print("Remova as notas menores que 7 e exiba a lista: ");
        Iterator<Double> iterator1 = notas.iterator();
        while(iterator1.hasNext()) {
            Double next = iterator1.next();
            if(next < 7) iterator1.remove();
        }
        System.out.println(notas);

        System.out.print("Apague toda a Lista: ");
        notas.clear();
        System.out.println(notas);

        System.out.println("Confira se a lista está vazia: " + notas.isEmpty());

        System.out.print("Crie uma lista chamada notas2: ");
        List<Double> notas1 = Arrays.asList(7d, 8.5, 9.3, 5d, 8d, 3.6);
        List<Double> notas2 = new LinkedList<>(notas1);
        System.out.println(notas2);

        System.out.println("Mostre a primeira nota da nova lista sem removê-lo: " + notas2.get(0));
        System.out.println("Mostre a primeira nota da nova lista removendo-o: " + notas2.remove(0));
        System.out.println("Lista notas1: "+ notas1);
        System.out.println("Lista notas2: "+ notas2);




    }
}
