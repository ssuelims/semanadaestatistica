"""Um professor precisa sortear bombons para diversos alunos.
Esses alunos serao sorteados rondomicamente.
o numero deve corresponder ao numero do diario"""


import random


# looping - iteraçao -  repetiçao - laço

while True:
    numero_aleatorio = random.randint(1,25)

# padrao snacke_case(pep - 8)

    sorteio_turma = random.randint(1,25) 
    resposta =input("deseja sortear outro numero?(s/n)").strip().lower()
    if resposta !="s":                                                                                                        
        print("encerrando o sorteio")
        break

    