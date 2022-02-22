package ClasseAtributoMetodoObjeto;

/**
 * Classe, atributo, método exemplo para o primeiro exercicio de POO, aula 3.
 */
class Carro {

    String cor, modelo;
    int volumeTanque;

    Carro() {

    }

    Carro(String cor, String modelo, int volumeTanque) {
        this.cor = cor;
        this.modelo = modelo;
        this.volumeTanque = volumeTanque;

    }

    void setCor(String cor) {
         this.cor = cor;
    }

    String getCor(){
        return cor;
    }

    void setModelo (String modelo){
        this.modelo = modelo;
    }

    String getModelo () {
        return modelo;
    }

    void setVolumeTanque (int volumeTanque) {
        this.volumeTanque = volumeTanque;
    }

    int getVolumeTanque() {
        return volumeTanque;
    }

    double totalValorTanque(double valorCombustivel) {
        return volumeTanque * valorCombustivel;
    }

}

