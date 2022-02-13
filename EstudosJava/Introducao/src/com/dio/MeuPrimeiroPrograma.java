package com.dio;//define pacote da classe


import com.dio.base.Order; //importa clase Order
//modificador de acesso, class, nome com letra maiuscula
public class MeuPrimeiroPrograma { //criaaclasse
    //criaometodo(publico com array de strings)
    public static void main(String[] args) {
        Order order = new Order( "code1234", 101);//cria variacao do tipo pedido e passa ordem
        System.out.println(order);//impressao do pedido
    }
}
