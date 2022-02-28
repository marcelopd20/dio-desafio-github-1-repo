package gof;

import gof.Facade.Facade;
import gof.Singleton.SingletonEager;
import gof.Singleton.SingletonLazy;
import gof.Singleton.SingletonLazyHolder;
import gof.Strategy.*;

public class Test {
    public static void main(String[] args) {

        //Singleton
        System.out.println("Singleton");
        SingletonLazy lazy = SingletonLazy.getInstancia();
        System.out.println(lazy);
        lazy = SingletonLazy.getInstancia();
        System.out.println(lazy);

        SingletonEager eager = SingletonEager.getInstancia();
        System.out.println(eager);
        eager = SingletonEager.getInstancia();
        System.out.println(eager);

        SingletonLazyHolder lazyHolder = SingletonLazyHolder.getInstancia();
        System.out.println(lazyHolder);
        lazyHolder = SingletonLazyHolder.getInstancia();
        System.out.println(lazyHolder);

        //Strategy
        System.out.println();
        System.out.println("Strategy");

        Comportamento defensivo = new ComportamentoDefensivo();
        Comportamento normal = new ComportamentoNormal();
        Comportamento agressivo = new ComportamentoAgressivo();


        Robo robo = new Robo();
        robo.setComportamento(normal);
        robo.mover();
        robo.setComportamento(defensivo);
        robo.mover();
        robo.mover();
        robo.setComportamento(agressivo);
        robo.mover();
        robo.mover();
        robo.mover();

        //Facade
        System.out.println();
        System.out.println("Facade:");

        Facade facade = new Facade();
        facade.migrarCliente("Venilton", "1472000");

    }
}
