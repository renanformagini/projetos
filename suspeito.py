suspeito = []

perguntas = [
    "Telefonou para a vitima ? ",
    "Esteve no local do crime ? ",
    "Mora perto da vítima ? ",
    "Devia para a vítima ? ", 
    "Ja trabalhou com a vítima ? "
]
respostaErrada = False

print("Responda as perguntas com sim ou não :")
for i in perguntas:
    resposta = input(i).lower()
    if resposta in ('sim','não'):
        if resposta =='sim':
            suspeito.append(1)
        else:
            suspeito.append(0)
    else:
        print("Desculpa, não entendi sua resposta ! Responda sim ou não !")
        respostaErrada = True
        break

if respostaErrada:
    pass
else:
    if len(suspeito) == 0 or len(suspeito) == 1:
        print("Inocente ")
    elif len(suspeito) == 2:
        print("suspeito")
    elif len(suspeito) == 3 or len(suspeito) == 4:
        print("Cúmplice")
    elif len(suspeito) == 5:
        print("Assaltante")
