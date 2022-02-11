lanches = [(), ('Cachorro quente', 4.00), ('X-Salada', 4.50), ('X-Bacon', 5.00), ('Torrada simples', 2.00),
           ('Refrigerante', 1.50)]

cod, quant = map(int, input().split())
total = (lanches[cod][1] * quant)
print(f'Total: R$ {total:.2f}')
