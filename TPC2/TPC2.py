def main():
    s = input("Escreva a frase:")
    texto = s.split(" ")
    count = 0
    somar = True
    for palavra in texto:
        if palavra.lower() == "on":
            somar = True
        elif palavra.lower() == "off":
            somar = False
        elif palavra == "=":
            print(count)
        elif somar == True:
            if palavra.isdigit():
                count += int(palavra)

main()
