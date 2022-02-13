package com.dio.base;//definição de onde a classe se encontra

/**
 * @author Marcelo Duarte
 * @version 1.0.0
 * @see int
 * @since Releases x.x
 *
 */
//definicao da classe
public class Order {
    //definição dos atributos
    private final String code;
    public final int totalValue;//instanciado

    /**
     * @param code  código do pedido
     * @param totalValue    valor total do pedido
     */

    private String[] items;
    //metodo construtor
    public Order(String code, int totalValue) {
        this.code = code;
        this.totalValue = totalValue;
        }
        //metodo para calcular taxas

    /**
     * Método for para estudo
     * @return retorna items da lista
     * @throws RuntimeException
     */
    public void printItems() throws RuntimeException {
        for (String i : items) {
            System.out.println(i);
        }
    }
}

