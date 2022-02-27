package Collections.Set;


import org.w3c.dom.ls.LSOutput;

import java.util.*;

/*/*
Crie uma conjunto contendo as cores do arco-íris e:
a) Exiba todas as cores o arco-íris uma abaixo da outra;
b) A quantidade de cores que o arco-íris tem;
c) Exiba as cores em ordem alfabética;
d) Exiba as cores na ordem inversa da que foi informada;
e) Exiba todas as cores que começam com a letra ”v”;
f) Remova todas as cores que não começam com a letra “v”;
g) Limpe o conjunto;
h) Confira se o conjunto está vazio;
 */
public class Exercicio1Set {
    public static void main(String[] args) {
        System.out.println("Crie uma conjunto contendo as cores do arco-íris e:");
        Set<Cor> arcoIris = new HashSet<>() {{
           add(new Cor("Vermelho"));
           add(new Cor("Alaranjado"));
           add(new Cor("Amarelo"));
           add(new Cor("Verde"));
           add(new Cor("Azul"));
           add(new Cor("Anil"));
           add(new Cor("Violeta"));
        }};

        System.out.println(arcoIris);
        System.out.println("a) Exiba todas as cores o arco-íris uma abaixo da outra: ");
        for (Cor cor: arcoIris) System.out.println(cor);
        System.out.println("b) A quantidade de cores que o arco-íris tem: ");
        System.out.println(arcoIris.size());
        System.out.println("c) Exiba as cores em ordem alfabética: ");
        Set<Cor> arcoIris1 = new TreeSet<>(new CompareCor());
        arcoIris1.addAll(arcoIris);
        for (Cor cor: arcoIris1) System.out.println(cor);

        System.out.println("d) Exiba as cores na ordem inversa da que foi informada;");
        Set<Cor> arcoIris2 = new TreeSet<>(new CompareCor().reversed());
        arcoIris2.addAll(arcoIris);
        for (Cor cor: arcoIris2) System.out.println(cor);
        System.out.println("e) Exiba todas as cores que começam com a letra ”v”: ");
        for (Cor cor: arcoIris) if (cor.getCor().contains("V")) System.out.println(cor);
        System.out.println("f) Remova todas as cores que não começam com a letra “v”: ");
        arcoIris.removeIf(cor -> cor.getCor().contains("V") == false);
        System.out.println(arcoIris);
        System.out.println("g) Limpe o conjunto: ");
        arcoIris.removeAll(arcoIris);
        System.out.println(arcoIris);
        System.out.println("h) Confira se o conjunto está vazio: " + arcoIris.isEmpty());
    }
}
class Cor implements Comparable<Cor> {
    private String cor;

    public Cor(String cor) {
        this.cor = cor;
    }

    public String getCor() {
        return cor;
    }

    @Override
    public String toString() {
        return cor;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Cor cor1 = (Cor) o;
        return cor.equals(cor1.cor);
    }

    @Override
    public int hashCode() {
        return Objects.hash(cor);
    }

    @Override
    public int compareTo(Cor cor) {
        return cor.compareTo(cor);
    }


}
class CompareCor implements Comparator<Cor> {
    @Override
    public int compare(Cor o1, Cor o2) {
        return o1.getCor().compareTo(o2.getCor());
    }
    @Override
    public Comparator<Cor> reversed() {
        return Comparator.super.reversed();
    }
}