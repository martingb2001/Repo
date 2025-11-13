nombres = ["Luis","Ana","Pedro"]
nombres.append("Maria")
while True:
    entrada = input("Ingresa un nombre (enter para terminar): ")
    if entrada == "":
        break
    nombres.append(entrada)
    print("Cantidad de nombres:", len(nombres))
    nombres.sort()
    print("Ordenados A->Z:", nombres)
    vocales = "aeiouAEIOU"
    nombres = [n for n in nombres if n[0] in vocales]
    print ("Cantidad tras eliminar:", len(nombres))
    nombres.sort(reverse=True)
    print ("Ordenados Z->A", nombres)