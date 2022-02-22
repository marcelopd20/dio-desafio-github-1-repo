package ClasseAtributoMetodoObjeto;

public class Main {
    public static void main(String[] args) {

        Carro carro1 = new Carro();

        carro1.setCor("Azul");
        carro1.setModelo("Cruze");
        carro1.setVolumeTanque(40);

        System.out.println(carro1.getModelo());
        System.out.println(carro1.getCor());
        System.out.println(carro1.getVolumeTanque());
        System.out.println(carro1.totalValorTanque(6.09));

        Carro carro2 = new Carro("Cinza", "Mercedes-Benz Classe C", 68);

        System.out.println(carro2.getModelo());
        System.out.println(carro2.getCor());
        System.out.println(carro2.getVolumeTanque());
        System.out.println(carro2.totalValorTanque(6.09));

    }
}
