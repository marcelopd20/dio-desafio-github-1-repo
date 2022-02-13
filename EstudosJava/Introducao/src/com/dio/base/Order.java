package com.dio.base;//definição de onde a classe se encontra

//definicao da classe
public class Order {
    //definição dos atributos
    private final String code;
    public final int totalValue;//instanciado

    private String[] items;
    //metodo construtor
    public Order(String code, int totalValue) {
        this.code = code;
        this.totalValue = totalValue;
        }
        //metodo para calcular taxas

    public void printItems() {
        int i = 0;
        while (i < items.length) {
            System.out.println(items[i]);
            i++;
        }
    }
}

