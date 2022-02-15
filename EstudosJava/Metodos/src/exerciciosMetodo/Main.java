package exerciciosMetodo;

public class Main {

    public static void main(String[] args) {

        //Calculadora:
        System.out.println("Exercicio calculadora:");
        Calculadora.soma(3, 6);
        Calculadora.subtracao(9,5);
        Calculadora.multiplicacao(3, 8);
        Calculadora.divisao(21, 3);

        //mensagem
        Mensagem.obterMensagem(9);
        Mensagem.obterMensagem(14);
        Mensagem.obterMensagem(1);
        Mensagem.obterMensagem(25);

        //Emprestimo
        System.out.println("Exercicio empréstimo");
        Emprestimo.calcular(1000, 2);
        Emprestimo.calcular(2000, Emprestimo.getDuasParcelas());
        Emprestimo.calcular(1000, 3);
        Emprestimo.calcular(1000, Emprestimo.getTresParcelas());
        Emprestimo.calcular(1000, 5);
    }

}
