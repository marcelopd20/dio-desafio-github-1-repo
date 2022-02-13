package com.dio;//define pacote da classe

import com.dio.base.Order; //importa clase Order

public class MeuPrimeiroPrograma { //criaaclasse
    //criaometodo(publico com array de strings)
    public static void main(String[] args) {
        Order order = new Order( "code1234");//cria variacao do tipo pedido e passa ordem
        System.out.println(order);//impressao do pedido
    }
}
