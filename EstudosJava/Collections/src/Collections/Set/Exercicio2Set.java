package Collections.Set;

import java.util.Comparator;
import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

/*
Crie uma classe LinguagemFavorita que possua os atributos nome, anoDeCriacao e IDE.
Em seguida, crie um conjunto com 3 linguagens e faça um programa que ordene esse
conjunto por:
a) Ordem de inserção;
b) Ordem natural(nome);
c) IDE;
d) Ano de criação e nome;
e) Nome, ano de criação e IDE;
Ao final, exiba as linguagens no console, um abaixo da outra.
*/
class Exercicio2Set {
    public static void main(String[] args) {
        System.out.println("Crie uma classe LinguagemFavorita que possua os atributos nome, anoDeCriacao e IDE.\n" +
                "Em seguida, crie um conjunto com 3 linguagens e faça um programa que ordene esse \n" +
                "conjunto por:");

        Set<LinguagemFavorita> linguagemFavorita = new HashSet<>() {{
           add(new LinguagemFavorita("Java", 1991, "IntelliJ"));
           add(new LinguagemFavorita("Python", 1990, "PyCharm"));
           add(new LinguagemFavorita("JavaScript", 1995, "NodeJS"));
        }};

        System.out.println("a) Ordem de inserção:");
        for (LinguagemFavorita linguagem: linguagemFavorita) System.out.println(linguagem);

        System.out.println("b) Ordem natural(nome):");
        Set<LinguagemFavorita> linguagemFavorita1 = new TreeSet<>(new ComparatorNome());
        linguagemFavorita1.addAll(linguagemFavorita);
        for (LinguagemFavorita linguagem: linguagemFavorita1) System.out.println(linguagem);

        System.out.println("c) IDE:");
        Set<LinguagemFavorita> linguagemFavorita2 = new TreeSet<>(new ComparatorIDE());
        linguagemFavorita2.addAll(linguagemFavorita);
        for (LinguagemFavorita linguagem: linguagemFavorita2) System.out.println(linguagem);

        System.out.println("d) Ano de criação e nome:");
        Set<LinguagemFavorita> linguagemFavorita3 = new TreeSet<>(new ComparatorAnoNome());
        linguagemFavorita3.addAll(linguagemFavorita);
        for (LinguagemFavorita linguagem: linguagemFavorita3) System.out.println(linguagem);

        System.out.println("e) Nome, ano de criação e IDE:");
        Set<LinguagemFavorita> linguagemFavorita4 = new TreeSet<>(new ComparatorNomeAnoIDE());
        linguagemFavorita4.addAll(linguagemFavorita);
        for (LinguagemFavorita linguagem: linguagemFavorita4) System.out.println(linguagem);

        System.out.println("Ao final, exiba as linguagens no console, um abaixo da outra:");
        for (LinguagemFavorita linguagem: linguagemFavorita4) System.out.println(linguagem.getNome());
    }


}

class LinguagemFavorita implements Comparator {
    private String nome;
    private int anoDeCriacao;
    private String iDE;

    public LinguagemFavorita(String nome, int anoDeCriacao, String iDE) {
        this.nome = nome;
        this.anoDeCriacao = anoDeCriacao;
        this.iDE = iDE;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getAnoDeCriacao() {
        return anoDeCriacao;
    }

    public void setAnoDeCriacao(int anoDeCriacao) {
        this.anoDeCriacao = anoDeCriacao;
    }

    public String getiDE() {
        return iDE;
    }

    public void setiDE(String iDE) {
        this.iDE = iDE;
    }

    @Override
    public String toString() {
        return "nome='" + nome + '\'' +
                ", anoDeCriacao=" + anoDeCriacao +
                ", iDE='" + iDE + '\'';
    }

    @Override
    public int compare(Object linguagem1, Object linguagem2) {
        return 0;
    }
}
class ComparatorNome implements Comparator<LinguagemFavorita> {
    @Override
    public int compare(LinguagemFavorita l1, LinguagemFavorita l2) {
        return l1.getNome().compareTo(l2.getNome());
    }
}
class ComparatorIDE implements Comparator<LinguagemFavorita> {
    @Override
    public int compare(LinguagemFavorita l1, LinguagemFavorita l2) {
        return l1.getiDE().compareTo(l2.getiDE());
    }
}
class ComparatorAnoNome implements Comparator<LinguagemFavorita> {
    @Override
    public int compare(LinguagemFavorita l1, LinguagemFavorita l2) {
        int ano = Integer.compare(l1.getAnoDeCriacao(), l2.getAnoDeCriacao());
        if (ano != 0) return ano;
        return l1.getNome().compareTo(l2.getNome());
    }
}
class ComparatorNomeAnoIDE implements Comparator<LinguagemFavorita> {
    @Override
    public int compare(LinguagemFavorita l1, LinguagemFavorita l2) {
        int nome = l1.getNome().compareTo(l2.getNome());
        if (nome != 0) return nome;
        int ano = Integer.compare(l1.getAnoDeCriacao(), l2.getAnoDeCriacao());
        if (ano != 0) return ano;
        return l1.getiDE().compareTo(l2.getiDE());
    }
}
