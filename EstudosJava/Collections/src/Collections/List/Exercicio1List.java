package Collections.List;
/*
Faça um programa que receba a temperatura média dos 6
primeiros meses do ano e armazene-as em uma lista.

Após isto, calcule a média semestral das temperaturas e
mostre todas as temperaturas acima desta média, e em que
mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2
– Fevereiro e etc).
 */


import com.sun.source.tree.UsesTree;

import java.util.*;



public class Exercicio1List {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        List<Mes> primeiroSemestre = new ArrayList<>(){{
            add(new Mes("Janeiro", null));
            add(new Mes("Fevereiro", null));
            add(new Mes("Março", null));
            add(new Mes("Abril", null));
            add(new Mes("Maio", null));
            add(new Mes("Junho", null));
        }};

        int count = 0;
        double soma = 0;

        do {
            System.out.print("Digite a temperatura do mes de " + primeiroSemestre.get(count).getMes() + ": ");
            primeiroSemestre.set(count, new Mes(primeiroSemestre.get(count).getMes(), scan.nextDouble()));
            soma += primeiroSemestre.get(count).getTemp();
            count++;
        } while (count < primeiroSemestre.size());
        double media = (soma/ primeiroSemestre.size());
        System.out.printf("A média de temperatura semestral foi: %.2f", media);
        System.out.println("Acima da média estão os meses: ");
        for (int i = 0; i < primeiroSemestre.size(); i++) {
            if (primeiroSemestre.get(i).getTemp() > media) {
                System.out.println((i+1) + " - " + primeiroSemestre.get(i).getMes());
            }
        }
    }




}
class Mes {
    public String mes;
    public Double temp;

    public Mes(String mes, Double temp) {
        this.mes = mes;
        this.temp = temp;
    }

    public String getMes() {
        return mes;
    }

    public Double getTemp() {
        return temp;
    }

    public void setTemp(Double temp) {
        this.temp = temp;
    }

    @Override
    public String toString() {
        return "Mes{" +
                "mes='" + mes + '\'' +
                ", temp=" + temp +
                '}';
    }
}
