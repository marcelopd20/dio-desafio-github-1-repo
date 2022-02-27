package Collections.Map;

import java.util.*;

/*
Dado os modelos dos carros e seus respectivos consumos na estrada, faça:
modelo = gol - consuma = 14,4km/l
modelo = uno - consuma = 15,6km/l
modelo = mobi - consuma = 16,1km/l
modelo = hb20 - consuma = 14,5km/l
modelo = kwid - consuma = 15,6km/l
 */
public class ExemploMap {
    //Map carrosPopulares2020 = new HashMap();
    //Map<String, Double> carrosPopulares = new HashMap<>();
    //HashMap<String, Double> carrosPopulares = new HashMap<>();
    //Map<String, Double> carrosPopulares = Map.of("gol", 14.4, "uno, 15.6, mobi, 16.1);

    public static void main(String[] args) {
        System.out.println("Crie um dicionário que relacione os modelos e seus respectivos consumos:");
        Map<String, Double> carrosPopulares = new HashMap<>(){{
           put("gol", 14.4);
           put("uno", 15.6);
           put("mobi", 16.1);
           put("hb20", 14.5);
           put("kwid", 15.6);
        }};
        System.out.println(carrosPopulares.toString());

        System.out.println("Substitua o consumo do gol por 15.2 km/l: ");
        carrosPopulares.put("gol", 15.2);
        System.out.println(carrosPopulares);

        System.out.println("Confira se o modelo tucson está no dicionário:" + carrosPopulares.containsKey("tucson"));

        System.out.println("Exiba o consumo do uno: " + carrosPopulares.get("uno"));

        //System.out.println("Exiba o terceiro modelo adicionado: " + carrosPopulares);

        System.out.println("Exiba os modelos: " + carrosPopulares.keySet());

        System.out.println("Exiba os consumos dos carros: " + carrosPopulares.values());

        System.out.println("Exiba o modelo mais econômico e seu consumo: ");
                Double consumoMaisEficiente = Collections.max(carrosPopulares.values());
                Set<Map.Entry<String, Double>> entries = carrosPopulares.entrySet();
                String modeloMaisEficiente;
                for(Map.Entry<String, Double> entry : entries) {
                    if (entry.getValue().equals(consumoMaisEficiente)){
                        modeloMaisEficiente = entry.getKey();
                        System.out.println(modeloMaisEficiente +" "+ consumoMaisEficiente);
                    }
                }

        System.out.println("Exiba o modelo menos econômico e seu consumo: ");
                Double consumoMenosEficiente = Collections.min(carrosPopulares.values());
                Set<Map.Entry<String, Double>> entries1 = carrosPopulares.entrySet();
                String modeloMenosEficiente;

                for(Map.Entry<String,Double> entry : entries1){
                    if (entry.getValue().equals(consumoMenosEficiente)) {
                        modeloMenosEficiente = entry.getKey();
                        System.out.println(modeloMenosEficiente + " " + consumoMenosEficiente);
                    }
                }

        System.out.println("Exiba a soma dos consumos: ");
                double soma = 0;
                for(Double entry: carrosPopulares.values()){
                    soma += entry;
                }
        System.out.println(soma);

        System.out.println("Exiba a média dos consumos:");
        System.out.println(soma/ carrosPopulares.size());

        System.out.println("Remova os modelos com o consumo igual a 15,6: ");
        Iterator<Double> iterator1 = carrosPopulares.values().iterator();
        while(iterator1.hasNext()) {
            if (iterator1.next().equals(15.6)) {iterator1.remove();
            }
        }
        System.out.println(carrosPopulares);

        System.out.println("Exiba todos os carros na ordem que foram informados: ");
        Map<String, Double> carrosPopulares1 = new LinkedHashMap<>(){{
            put("gol", 14.4);
            put("uno", 15.6);
            put("mobi", 16.1);
            put("hb20", 14.5);
            put("kwid", 15.6);
        }};
        System.out.println(carrosPopulares1.toString());

        System.out.println("Exiba o dicionário ordenado pelo modelo: ");
        Map<String,Double> carrosPopulares2 = new TreeMap<>(carrosPopulares1);
        System.out.println(carrosPopulares2.toString());

        System.out.println("Apague o dicionário de carros:");
        carrosPopulares.clear();
        System.out.println(carrosPopulares);

        System.out.println("Confira se a lista está vazia: " + carrosPopulares.isEmpty());
    }


}
