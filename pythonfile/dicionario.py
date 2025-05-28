#EXERCICIO SOBRE DICIONARIO!!

pessoa = {
    "nome":"João",
    "idade":21,
    "altura":"1,70",
    "peso":"74kg",
    "endereços":[
            {"rua":"taltaltal","numero":31}, 
            {"rua":"blablabla","numero":23},       
    ],
    "estado civil":"solteiro"
}

for i in pessoa:
    print(i,pessoa[i])