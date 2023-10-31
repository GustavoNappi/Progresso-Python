notas = [10, 20, 40, 30]


i = 0
total = 0
qtd = len(notas)
while i < qtd : 
    total = total + notas[i]
    i = i + 1


    print ("O total das notas é ", total)
    media = total/qtd 

    print ("E a média é :", media)