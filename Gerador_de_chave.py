from random import randint
import MDC

def Gerador_de_chave:

    def __init__(self,primeiro_primo,segundo_primo,value,n):
        lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        primeiro = lista[random.randint(0,10)]
        while Primeiro_primo == Segundo_primo:
            Segundo_primo = lista[random.randint(0,10)]

        n = Segundo_primo * Primeiro_primo
'''
######### Cálculo da função totiente #################
'''
totiente = (Segundo_primo - 1)*(Primeiro_primo - 1)
'''
######### GERACAO DA CHAVE PUBLICA #################
'''
for i in range (0,totiente,1):
    if  MDC(totiente,i) == 1:
        if i != totiente:
            value =  i
key = [value, totiente]
'''
#########        FIM DA FUNCAO     #################
'''
