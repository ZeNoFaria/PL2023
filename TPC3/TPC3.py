import re
import pprint

def frequenciaPorAno(er,dicA):
    ficheiro = open("processos.txt")
    for linha in ficheiro:
        if(re.match(er,linha)):
            data = re.split("-",re.match(er,linha).group("data"))
            ano = data[0]
            if ano not in dicA.keys():
                dicA[ano] = 1
            else:
                dicA[ano] += 1

def getSeculo(ano):
    resto = int(ano) % 100
    return((int(ano) - resto)/100 -1)

def nomesPropriosPorSeculo(dicB,er):
    ficheiro = open("processos.txt")
    for linha in ficheiro:
        if(re.match(er,linha)):
            data = re.split("-",re.match(er,linha).group("data"))
            ano = data[0]
            sec = getSeculo(ano)
            nome = re.split(" ",re.match(er,linha).group("nome"))
            nomeProprio = nome[0]
            if sec not in dicB:
                dicB[sec] = {}
                if nomeProprio not in dicB[sec]:
                    dicB[sec][nomeProprio] = 1
                else:
                    dicB[sec][nomeProprio] += 1
            else:
                if nomeProprio not in dicB[sec]:
                    dicB[sec][nomeProprio] = 1
                else:
                    dicB[sec][nomeProprio] += 1
    pprint.pprint(dicB)

def apelidosPorSeculo(dicApelidos,er):
    ficheiro = open("processos.txt")
    for linha in ficheiro:
        if(re.match(er,linha)):
            data = re.split("-",re.match(er,linha).group("data"))
            ano = data[0]
            sec = getSeculo(ano)
            nome = re.split(" ",re.match(er,linha).group("nome"))
            apelido = nome[len(nome)-1]
            if sec not in dicApelidos:
                dicApelidos[sec] = {}
                if apelido not in dicApelidos[sec]:
                    dicApelidos[sec][apelido] = 1
                else:
                    dicApelidos[sec][apelido] += 1
            else:
                if apelido not in dicApelidos[sec]:
                    dicApelidos[sec][apelido] = 1
                else:
                    dicApelidos[sec][apelido] += 1
    pprint.pprint(dicApelidos)

def top5Nomes(dicTop5Nomes,er):
    ficheiro = open("processos.txt","r")
    for linha in ficheiro:
        if(re.match(er,linha)):
            nome = re.split(" ",re.match(er,linha).group("nome"))
            if nome[0] not in dicTop5Nomes.keys():
                dicTop5Nomes[nome[0]] = 1
            else:
                dicTop5Nomes[nome[0]] += 1
    print(sorted(dicTop5Nomes.items(),key=lambda x:x[1],reverse=True)[:5])

def top5Apelidos(dicTop5Apelidos,er):
    ficheiro = open("processos.txt","r")
    for linha in ficheiro:
        if(re.match(er,linha)):
            nome = re.split(" ",re.match(er,linha).group("nome"))
            apelido = nome[len(nome)-1]
            if apelido not in dicTop5Apelidos.keys():
                dicTop5Apelidos[apelido] = 1
            else:
                dicTop5Apelidos[apelido] += 1
    print(sorted(dicTop5Apelidos.items(),key=lambda x:x[1],reverse=True)[:5])

def frequenciaRelacao(dicParentesco,er):
    ficheiro = open("processos.txt","r")
    for linha in ficheiro:
        if(re.match(er,linha)):
            obs = re.match(er,linha).group("observacoes")
            regex1 = re.compile(r",(?P<parentesco>[a-zA-z]+[ ]*[a-zA-Z]*)\.")
            regex2 = re.compile(r"")
            if re.search(regex1,obs) != None:
                parentesco = regex1.search(obs).group("parentesco")
                if parentesco not in dicParentesco.keys():
                    dicParentesco[parentesco] = 1
                else:
                    dicParentesco[parentesco] += 1
    pprint.pprint(dicParentesco)

def main():
    er = re.compile(r"(?P<pasta>\d+)::(?P<data>[0-9\-]*)::(?P<nome>[\w ]*)::(?P<pai>[\w ]*)::(?P<mae>[\w ]*)::(?P<observacoes>[^:]*)")
    dicA = {}
    dicNomes = {}
    dicApelidos = {}
    dicTop5Nomes = {}
    dicTop5Apelidos = {}
    dicParentesco = {}
    frequenciaPorAno(er,dicA)
    nomesPropriosPorSeculo(dicNomes,er)
    apelidosPorSeculo(dicApelidos,er)
    top5Nomes(dicTop5Nomes,er)
    top5Apelidos(dicTop5Apelidos,er)
    frequenciaRelacao(dicParentesco,er)


main()