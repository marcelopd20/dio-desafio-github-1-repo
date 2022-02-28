package gof.Singleton;
/**
 * gof.Singleton "Eager"
 * @author marcelopd20

 */
public class SingletonEager {

    private static SingletonEager instancia = new SingletonEager();

    private SingletonEager() {
        super();
    }

    public static SingletonEager getInstancia (){
        return instancia;
    }
}
