package com.dio.base;//definição de onde a classe se encontra

//definicao da classe
public class Order {
    //definição dos atributos
    private final String code;
    public final int totalValue;//instanciado
    //metodo construtor
    public Order(String code, int totalValue) {
        this.code = code;
        this.totalValue = totalValue;
        }
        //metodo para calcular taxas
    public double calculateFee() {
        switch (totalValue) {
            case 100:
                return totalValue * 0.99;
            case 200:
                return totalValue * 1.99;
            default:
                return totalValue;
        }
    }
}

