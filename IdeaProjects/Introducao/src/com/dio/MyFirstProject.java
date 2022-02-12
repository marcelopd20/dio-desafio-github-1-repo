package com.dio;

import com.dio.base.Order;

import java.math.BigDecimal;

public class MyFirstProject {

    public static void main(String[] args) {
        Order o = new Order("code1234", 200);
        System.out.println(o.calculateFee());
    }
}