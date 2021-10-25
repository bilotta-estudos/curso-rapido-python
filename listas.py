#Listas são similares aos arrays em javascript

nums = [1, 2, 3]
print(nums)

#Adicionando novos elementos na lista
nums.append(4)
nums.append(5)

print(nums)

#Verificando o tamanho da lista 
print(f'A lista possui {len(nums)} elementos')

#Alterando o valor de um elemento da lista
nums[0] = 100
print(nums)

#Inserindo valor em uma determinada posição
nums.insert(1, -200)
print(nums)

#Apresentando o valor de uma determinada posição (index)
print(f'O último elemento da lista é: {nums[5]}')
print(f'O último elemento da lista é: {nums[-1]}')

#Verificar o index através do valor
index = nums.index(2)
print(f'O index de 2 é: {index}')

#Verificar se um item está na lista
nomes = ['Ana', 'Nicole', 'José']
print('Rebeca' in nomes)
print('Nicole' in nomes)

#Verificar se um item não está na lista
nomes = ['Ana', 'Nicole', 'José']
print('Rebeca' not in nomes)
print('Nicole' not in nomes)

#Criando uma sublista (inicio é inclusivo e final exclusivo)
print(nomes[0:2])
print(nomes [:-1])
print(nomes[:])
print(nomes[0:])

#Criando uma sublista pegando de dois em dois elementos
nomes = ['Ana', 'Nicole', 'José', 'Marco', 'Nivaldo', 'Túlio']
print(nomes[::2])



#Removendo um item da lista a partir do valor
nums.remove(-200)
print(nums)

#removendo um item da lista pelo index
del nomes[1]
print(nomes)

#Revertendo a lista
nums.reverse()
print(nums)

