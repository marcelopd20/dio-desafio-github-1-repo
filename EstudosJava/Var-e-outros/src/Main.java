public class Main {
    public static void main(String[] args) {

        int i;
        //int i;repete variavel ja declarada
        int I;
        //int 1a;começa com numero
        int _1a;//não é uma boa prática
        int $aq;//não é uma boa prática

        i = 5;
        I = 10;
        _1a = 20;
        $aq = 7;

        final int j = 10;
        //j = 15; nao pode, j é final
        int asrn24678md;
        //int asrn2456 78md; espaço não é aceito
        int asrn2$4678_md = 10;
        //int arsn2%4678; uso de caracter nao aceito

        asrn24678md = 100;
        asrn2$4678_md = 10;

        int quantidadeProduto = 50;
        //int QuantidadeProduto; nao segue boa pratica
        final int NUMERO_TENTATIVAS =5;
        //final int numeroTentativas = 5; como é final oprtar por uso de _ e maiusculo
        int QUANTIDADE_OPCOES = 25;//não é boa pratica pois nao é final
        //int qtdProd; variavel com nome pouco claro

        System.out.println(i);
        System.out.println(I);
        System.out.println(_1a);
        System.out.println($aq);

        System.out.println(j);
        System.out.println(asrn24678md);
        System.out.println(asrn2$4678_md);

        System.out.println(quantidadeProduto);
        System.out.println(NUMERO_TENTATIVAS);
        System.out.println(QUANTIDADE_OPCOES);
    }

}
