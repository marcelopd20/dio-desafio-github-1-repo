package com.dio.base;//definição de onde a classe se encontra

import java.math.BigDecimal;//import de classe de pacote
//definicao da classe
public class Order {
    //definição dos atributos
    private final String code;
    public final BigDecimal totalValue;//instanciado
    //metodo construtor
    public Order(String code, BigDecimal totalValue) {
        this.code = code;
        this.totalValue = totalValue;
        }
        //metodo para calcular taxas
    public BigDecimal calculateFee() {
        return this.totalValue.multiply(new BigDecimal("0.99"));
        }
}

