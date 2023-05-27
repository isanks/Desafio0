import array

array=[]
menor_diff = float('inf')
listadiff = []
diff = []
valor = int(input("Digite um numero: "))
print("Informe 0 pra finalizar e realizar a saida!")


while(valor != 0):
    array.append(valor)
    valor= int(input("Digite um numero: ")) 
array.sort()  
for i in range(len(array) - 1):
    diff = abs(array[i] - array[i + 1]) 
    if diff < menor_diff:  
        menor_diff = diff 
        listadiff = [(array[i], array[i + 1])] 
    elif diff == menor_diff:  
        listadiff.append((array[i], array[i + 1]))
        


print(listadiff)