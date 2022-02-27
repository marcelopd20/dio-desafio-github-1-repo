package Collections.Set;

import java.util.*;

/* Dada as seguintes informações sobre séries crie um conjunto
e ordene este conjunto exibindo:
nome - genero - tempo de episódio
Série 1: nome: got, genero: fantasia, tempoEpisodio: 60
Série 2: nome: dark, genero: drama, tempoEpisodio: 60
Série 3: = nome: that 70's show, genero: comédia, tempoEpisódio: 25
 */
public class ExemploOrdenacaoSet {
    public static void main(String[] args) {


        System.out.println("--\tOrdem Aleatória\t--");
        Set<Serie> minhasSeries = new HashSet<>(){{
            add(new Serie("got", "fantasia", 60));
            add(new Serie("dark", "drama", 60));
            add(new Serie("that 70's show" , "comédia", 25));
        }};
        for(Serie serie: minhasSeries)System.out.println(serie.getNome() + " - " +
                serie.getGenero() + " - " + serie.getTempoEpisodio());

        System.out.println("--\tOrdem Inserção\t--");
        Set<Serie> minhasSeries1 = new LinkedHashSet<>(){{
            add(new Serie("got", "fantasia", 60));
            add(new Serie("dark", "drama", 60));
            add(new Serie("that 70's show" , "comédia", 25));
        }};
        for (Serie serie: minhasSeries1) System.out.println(serie.getNome() + " - " +
                serie.getGenero() + " - " + serie.getTempoEpisodio());


        System.out.println("--\tOrdem natural (Tempo Episódio)\t--");
        Set<Serie> minhasSeries2 = new TreeSet<>(minhasSeries1);
        for(Serie serie: minhasSeries2) System.out.println(serie.getNome() + " - " + serie.getGenero() +
                " - " + serie.getTempoEpisodio());

        System.out.println("--\tOrdem Nome/Genero/TempoEpisodio\t--");
        Set<Serie> minhasSeries3 = new TreeSet<>(new ComparatorNomeGeneroTempoEpisodio());
        minhasSeries3.addAll(minhasSeries);
        for (Serie serie: minhasSeries3) System.out.println(serie.getNome() + " - " + serie.getGenero() + " - " +
                serie.getTempoEpisodio());

        System.out.println("--\tOrdem Genêro\t--");
        Set<Serie> minhasSeries4 = new TreeSet<>(new ComparatorGenero());
        minhasSeries4.addAll(minhasSeries);
        for (Serie serie: minhasSeries4) System.out.println(serie.getNome() + " - " + serie.getGenero() + " - " +
                serie.getTempoEpisodio());

        System.out.println("--\tOrdem Tempo\t--");
        Set<Serie> minhasSeries5 = new TreeSet<>(new ComparatorTempo());
        minhasSeries5.addAll(minhasSeries);
        for (Serie serie: minhasSeries5) System.out.println(serie.getNome() + " - " + serie.getGenero() + " - " +
                serie.getTempoEpisodio());



    }
}
class Serie implements Comparable<Serie> {
    private String nome;
    private String genero;
    private Integer tempoEpisodio;

    public Serie(String nome, String genero, Integer tempoEpisodio) {
        this.nome = nome;
        this.genero = genero;
        this.tempoEpisodio = tempoEpisodio;
    }

    public String getNome() {
        return nome;
    }

    public String getGenero() {
        return genero;
    }

    public Integer getTempoEpisodio() {
        return tempoEpisodio;
    }

    @Override
    public String toString() {
        return "{" +
                "nome='" + nome + '\'' +
                ", genero='" + genero + '\'' +
                ", tempoEpisodio=" + tempoEpisodio +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Serie serie = (Serie) o;
        return nome.equals(serie.nome) && genero.equals(serie.genero) && tempoEpisodio.equals(serie.tempoEpisodio);
    }

    @Override
    public int hashCode() {
        return Objects.hash(nome, genero, tempoEpisodio);
    }

    @Override
    public int compareTo(Serie serie) {
        int tempoEpisodio = Integer.compare(this.getTempoEpisodio(), serie.tempoEpisodio);
        if (tempoEpisodio != 0) return tempoEpisodio;
        return this.getGenero().compareTo(serie.getGenero());

    }
}
class ComparatorNomeGeneroTempoEpisodio implements Comparator<Serie> {
    @Override
    public int compare(Serie s1, Serie s2) {
        int nome = s1.getNome().compareTo(s2.getNome());
        if (nome != 0) return nome;
        int genero = s1.getGenero().compareTo(s2.getGenero());
        if (genero != 0) return genero;
        return Integer.compare(s1.getTempoEpisodio(), s2.getTempoEpisodio());
    }
}

class ComparatorGenero implements Comparator<Serie> {
    @Override
    public int compare(Serie s1, Serie s2) {
        int genero = s1.getGenero().compareTo(s2.getGenero());
        return genero;
    }
}
 class ComparatorTempo implements Comparator<Serie>{
     @Override
     public int compare(Serie s1, Serie s2) {
        int tempo = Integer.compare(s1.getTempoEpisodio(), s2.getTempoEpisodio());
        if (tempo == 0) return s1.getNome().compareTo(s1.getNome());
        return tempo;
     }
 }