package com.dio.base;//classe que representa o pedido

public class Order {
    //código do pedido
    private final String code;
    //criação do construtor
    public Order(String code){//instanciado
        this.code = code; //atributo recebe codigo que passou pelo metodo construtor
    }

    @Override //metodo sobrescrito
    public String toString() {//metodo de string responsavel por formatar iompressao do pedido
        return "Order={" +
                "code=" + code + "'" +
                "}";
    }
}
