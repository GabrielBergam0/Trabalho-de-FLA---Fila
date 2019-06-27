fila_normal = []
fila_prioritaria = []
fila_gestante = []

#criação das filas ------------------------------------------------------

print("Bem vindo ao meu simulador de fila!Meu criador é Gabriel Bergamo")

#introdução--------------------------------------------------------------

escolha = int(input("Digite 2 para simular e 1 para adicionar mais um: "))

#pedindo a fila de escolha-----------------------------------------------

while escolha != 2:
    print("Digite para adicionar uma pessoa a respectiva fila: 1-Fila normal , 2-Fila prioritária , 3-Fila gestante")
    print("__"*40)
    decisao = int(input("Digite sua decisão aqui: "))
    if decisao == 1:
        fila_normal.append("@")
        print("Fila normal: ",fila_normal)
        print("Fila prioritaria: ",fila_prioritaria)
        print("Fila gestante: ",fila_gestante)
    elif decisao == 2:
        fila_prioritaria.append("@")
        print("Fila normal: ",fila_normal)
        print("Fila prioritária: ",fila_prioritaria)
        print("Fila gestante: ",fila_gestante)
    elif decisao == 3:
        fila_gestante.append("@")
        print("Fila normal: ",fila_normal)
        print("Fila prioritária: ",fila_prioritaria)
        print("Fila gestante: ",fila_gestante)
    print("__"*40)

#todo o mecanismo para o funcionamento------------------------------------
    
    escolha = int(input("Digite 2 para simular e 1 para adicionar mais um: "))
#uso do while para deixar adicionar pessoas infinitamente nas filas-------

else:
    del fila_prioritaria
    fila_prioritaria = []
    print("Fila normal: ",fila_normal)
    print("Fila prioritária: ",fila_prioritaria)
    print("Fila gestante: ",fila_gestante)
    print("__"*40)
    del fila_gestante
    fila_gestante = []
    print("Fila normal: ",fila_normal)
    print("Fila prioritária: ",fila_prioritaria)
    print("Fila gestante: ",fila_gestante)
    print("__"*40)
    del fila_normal
    fila_normal = []
    print("Fila normal: ",fila_normal)
    print("Fila prioritária: ",fila_prioritaria)
    print("Fila gestante: ",fila_gestante)

#mecanismo para 'rodar' a fila,removendo as pessoas------------------------
