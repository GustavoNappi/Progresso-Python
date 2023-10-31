idade = 16
maior_de_idade = idade >= 18 
menor_de_idade = not maior_de_idade

##not or and operadores logicos

#print("idade da pessoa:", idade)
#print("é maior de idade:", maior_de_idade)
#print("Menor de idade:", menor_de_idade)

#and
#usuario_correto = True 
#senha_correta = True
#sucesso = usuario_correto and senha_correta
#print("Login Bem Sucedido", sucesso)

#or

idade = 12
idade_minima = 12 or 15
acompanhada_pelos_pais = True

pode_assistir = idade>= idade_minima or acompanhada_pelos_pais

print(pode_assistir)