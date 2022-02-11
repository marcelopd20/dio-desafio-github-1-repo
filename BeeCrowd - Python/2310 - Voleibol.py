"""Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas tentativas de
saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques tiveram sucesso
(resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.

Entrada
A entrada é dada pelo número de jogadores N (1 ≤ N ≤ 100), seguido pelo nome de cada um dos jogadores. Abaixo do nome de cada jogador,
seguem duas linhas com três inteiros cada. Na primeira linha S, B e A (0 ≤ S,B,A ≤ 10000) representam a quantidade de tentativas de
saques, bloqueios e ataques e na segunda linha, S1, B1 e A1 (0 ≤ S1 ≤ S; 0 ≤ B1 ≤ B; 0 ≤ A1 ≤ A) com o número de saques, bloqueios e
ataques deste jogador que tiveram sucesso.

Saída
A saída deve conter o percentual total de saques, bloqueios e ataques do time todo que resultaram em pontos, conforme mostrado no
exemplo."""
time = dict()
ST = BT = AT = SST = BST = AST = 0

for c in range(int(input(''))):
    N = str(input())
    S, B, A = [int(x) for x in input().split()]
    S1, B1, A1 = [int(x) for x in input().split()]
    time[N] = [S, B, A], [S1, B1, A1]

for k, v in time.items():
    ST += v[0][0]
    BT += v[0][1]
    AT += v[0][2]
    SST += v[1][0]
    BST += v[1][1]
    AST += v[1][2]
print(f"Pontos de Saque: {SST/ST*100:.2f} %. \n"
f"Pontos de Bloqueio: {BST/BT*100:.2f} %. \n"
f"Pontos de Ataque: {AST/AT*100:.2f} %.")
