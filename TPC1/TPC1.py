import matplotlib.pyplot as mpl

def doencaPorSexo(dic):
    nf = 0
    nm = 0
    for p in dic:
        if p[1] == 'M':
            nm+=1
        else:
            nf+=1
    temp = {"Masculino":nm,"Feminino":nf}
    print(temp)

def getCategoria(idade,x):
    resto = idade%x
    return (idade-resto,idade-resto+4)

def doencaPor(dic,a,b):
    dicionario = {}
    for p in dic:
        colesterol = int(p[a])
        categoria = getCategoria(colesterol,b)
        aux = {categoria:p}
        if categoria not in dicionario.keys():
            dicionario[categoria] = [aux[categoria]]
        else:
            dicionario[categoria].append(aux[categoria])
    keys = dicionario.keys()
    x = 0
    diciotemp = {}
    for key in keys:
        x = len(dicionario.get(key))
        diciotemp[key] = x
    #print(dict(sorted(diciotemp.items())))
    #imprimeTabela(dict(sorted(diciotemp.items())))
    imprimeGrafico(dict(sorted(diciotemp.items())))

def doencaPorIdadeOuColesterol(dic,x):
    if x == 0:
        doencaPor(dic,0,5)
    elif x == 1:
        doencaPor(dic,3,10)

def imprimeTabela(dic):
    print("Valores   Quantidade")
    keys = dic.keys()
    for key in keys:
        print(key , " " ,dic[key])

def imprimeGrafico(dic):
    keys = list(dic.keys())
    lista = []
    for key in keys:
        lista.append(str(key))
    values = list(dic.values())
    mpl.figure(figsize=(10, 5))
    mpl.bar(lista,values)
    mpl.show()

def abrir():
    ficheiro = open("myheart.csv","r")
    ficheiro.readline()
    tem = []
    ntem = []
    for linha in ficheiro:
        list = linha.strip('\n').split(',')
        if list[5] == '1':
            tem.append(list)
        else:
            ntem.append(list)
            
    dic = {"temDoenca" : tem, "naotemDoenca" : ntem}
    x = int(input("Idade->0\nColesterol->1\n"))
    doencaPorIdadeOuColesterol(dic["temDoenca"],x)
    ficheiro.close()

abrir()
