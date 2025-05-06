# num1 = input("digite um numero: ")
# num2 = input("digite um numero: ")

def media(lista):

    total = 0
    for i in lista: 
        
        total += i

    media = total / len(lista)
    return media

numeros = [6, 8, 9, 5]
           
print(media(numeros))