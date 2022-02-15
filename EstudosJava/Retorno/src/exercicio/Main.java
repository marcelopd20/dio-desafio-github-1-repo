package exercicio;

public class Main {

    public static void main(String[] args) {

        //Retornos
        System.out.println("Exercício retornos:");

        double areaQuadrado = Quadrilatero.area(3);
        System.out.println("Área do quadrado: "+ areaQuadrado);

        double areaRetangulo = Quadrilatero.area(5d, 3d);
        System.out.println("Área do retângulo: "+ areaRetangulo);

        double areaTrapezio = Quadrilatero.area(7, 8, 9);
        System.out.println("Área do retângulo: "+ areaTrapezio);

        double areaLosango = Quadrilatero.area(2f,10f);
        System.out.println("Área do Losango: "+ areaLosango);

    }

}
