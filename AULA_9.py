total = 0
while True: 
     valor = float(input("DIGITE O VALOR DA COMPRA"))
     total = total + valor

        continuar = (input("deseja continuar o programa? S/n"))
        if continuar != "S":
            break 
print("o valor total da compra", total)
   