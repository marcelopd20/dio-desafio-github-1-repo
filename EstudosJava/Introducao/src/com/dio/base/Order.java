package com.dio.base;//definição de onde a classe se encontra

//definicao da classe
public class Order {
    //definição dos atributos
    private final String code;
    public final double totalValue;//instanciado
    //metodo construtor
    public Order(String code, double totalValue) {
        this.code = code;
        this.totalValue = totalValue;
        }
        //metodo para calcular taxas
    public double calculateFee() {
        if (totalValue > 100){
            return totalValue * 0.99;
        } else {
            return totalValue;
        }
    }
}

