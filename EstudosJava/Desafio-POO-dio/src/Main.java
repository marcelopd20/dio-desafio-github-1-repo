import desafio.dominio.*;

import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        Curso curso1 = new Curso();
        curso1.setTitulo("Curso Java");
        curso1.setDescricao("Descrição curso Java");
        curso1.setCargaHoraria(8);

        Curso curso2 = new Curso();
        curso2.setTitulo("Curso JS");
        curso2.setDescricao("Descrição curso JS");
        curso2.setCargaHoraria(4);

        Mentoria mentoria1 = new Mentoria();
        mentoria1.setTitulo("Mentoria Java");
        mentoria1.setDescricao("Descrição mentoria Java");
        mentoria1.setData(LocalDate.now());

        Mentoria mentoria2 = new Mentoria();
        mentoria2.setTitulo("Mentoria JS");
        mentoria2.setDescricao("Descrição mentoria JS");
        mentoria2.setData(LocalDate.now());
        Conteudo conteudo = new Curso();
        Conteudo conteudo1 = new Mentoria();
        /*
        System.out.println(curso1);
        System.out.println(curso2);
        System.out.println(mentoria1);
        System.out.println(mentoria2);
         */

        Bootcamp bootcamp1 = new Bootcamp();
        bootcamp1.setNome("Bootcamp Java Developer");
        bootcamp1.setDescricao("Descrição Bootcamp Java Developer");
        bootcamp1.getConteudos().add(curso1);
        bootcamp1.getConteudos().add(curso2);
        bootcamp1.getConteudos().add(mentoria1);

        Dev devMarcelo = new Dev();
        devMarcelo.setNome("Marcelo");
        devMarcelo.inscreverBootcamp(bootcamp1);
        System.out.println("Conteudos Inscritos Marcelo: " + devMarcelo.getConteudosInscricao());

        devMarcelo.progredir();

        System.out.println("Conteudos Inscritos Marcelo: " + devMarcelo.getConteudosInscricao());
        System.out.println("Conteudos Concluídos Marcelo: " + devMarcelo.getConteudosConcluidos());
        System.out.println("XP: " + devMarcelo.calcularTotalXp());

        System.out.println(" ---------------- ");

        Dev devLarissa = new Dev();
        devMarcelo.setNome("Larissa");
        devLarissa.inscreverBootcamp(bootcamp1);
        System.out.println("Conteudos Inscritos Larissa: " + devLarissa.getConteudosInscricao());
        devLarissa.progredir();
        devLarissa.progredir();
        devLarissa.progredir();
        System.out.println("Conteudos Inscritos Larissa: " + devLarissa.getConteudosInscricao());
        System.out.println("Conteudos Concluídos Larissa: " + devLarissa.getConteudosConcluidos());
        System.out.println("XP: " + devLarissa.calcularTotalXp());



    }

}
