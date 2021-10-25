
#Python é uma linguagem com tipagem dinâmica, como javascript.
#Na documentação é informado que a linguagem é fortemente tipada e de tipagem dinâmica.

#Tipagem dinâmica => A variavel pode receber qualquer tipo de valor, alterar o valor
#para outro tipo a qualquer momento.

#Fortemente tipada => O interpretador não assume a responsabilidade de escolher qual ação
#tomar em determinadas situações (como no exemplo abaixo), gerando erro.
#contatenação com a função str

texto = 'Sua idade é: '
idade = 23
print(texto + str(idade))

#Uma forma melhor de realizar a concatenação utilizando o fString
print(f'{texto} {idade}')

#Escrevendo três vezes a mesma frase
saudacao = 'Bom dia '
print(3 * saudacao)

#Não temos constantes no Python, mas a convenção pede para as variáveis serem escritas
#com letra maiúscula

PI = 3.14
raio = float(input('Digite a raio para o cálculo da área:'))
area = PI * pow(raio, 2)
print(f'A área é: {area}')

a = 2
b = 3
print(a + b)

#Passou a ser uma String
a = 'Agora sou uma string!'

print(a)

#Se tentarmos concaternar uma String (a) com um Inteiro (b) vai gerar um erro, pois
#o python não assuma a responsabilidade de definir qual decisão tomar (Se quiser ver o
# erro é só descomentar a linha abaixo).
#print (a + b)




