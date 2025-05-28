perguntas = [
    {
        "pergunta" : "Qual o melhor time do mundo? :p\n",
        "alternativas" : ["os bambi", "a porcalhada", "O TIMÃO MALANDRO","real madrid" ],
        "resposta" : "O TIMÃO MALANDRO",
    },
    {
        "pergunta" : "O fim é?",
        "alternativas" : ["triste", "sempre o mesmo", "todas as alternativas"],
        "resposta" : "todas as alternativas",


    },

]
for i in perguntas:
    print( i["pergunta"])

    for i ,alternativas in enumerate(i["alternativas"]):
        print (f"{i})", alternativas)

    escolha = input("\nDigite a alternativa:")

    if escolha == (i["resposta"]):
        print("\nVAI CORINTHIANS NO BAGULHO")
    else:
        print("ERROU MALANDRO! Vai estudar futebol! 😆")

