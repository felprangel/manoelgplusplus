import sys

#Lê o argumento passado no cmd
nome_arquivo = sys.argv[1]

#Printa uma ajuda no cmd caso o usuário use -h ou --help como argumento
if nome_arquivo == "-h" or nome_arquivo == '--help':
	print("Sintaxe 'python interpreter.py [arquivo]’")
	sys.exit()
else:
	#Abre o arquivo caso o usuário tenha passado o nome de uma arquivo como argumento
	arquivo = open(nome_arquivo, "r")

#Define a variável que recebe o binário
binario=""

#percorre as linhas do arquivo e verifica a sintaxe da linguagem
linhas = arquivo.readlines()
for x in range(0,len(linhas)):
    if linhas[x] == "bom demaize" or linhas[x] == "bom demaize\n":
        binario = binario + "1"
    elif linhas[x]=="olha se voce nao me ama" or linhas[x]=="olha se voce nao me ama\n":
        binario = binario + "0"
    else:
        raise SyntaxError("Você não pode usar outra coisa além de 'bom demaize' ou 'olha se voce nao me ama'. Tem certeza que cada frase está em uma linha separada?")
    
#transforma o binário em texto
d=int(binario, 2)
l=(d.bit_length() + 7)//8
n=d.to_bytes(l,"big")
t=n.decode()
arquivo.close()

#cria um arquivo python e cola o texto nele
g=open("programme_made_by_compiler_do_not_touch.py","w")
g.write(t)
g.close()

#executa o programa
exec(open("programme_made_by_compiler_do_not_touch.py").read())
open("programme_made_by_compiler_do_not_touch.py").close()