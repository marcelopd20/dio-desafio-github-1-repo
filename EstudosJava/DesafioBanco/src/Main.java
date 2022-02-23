public class Main {

    public static void main(String[] args) {
        Cliente marcelo = new Cliente();
        marcelo.setNome("Marcelo");


        Conta cc = new ContaCorrente(marcelo);
        Conta cp = new ContaPoupanca(marcelo);


        cc.depositar(100);
        cc.transferir(100,cp);

        cc.imprimirExtrato();
        cp.imprimirExtrato();
    }
}
