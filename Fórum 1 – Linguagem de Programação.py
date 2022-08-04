# Exercicio A
tabuada=int(input("Tabuada do numero: "))
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )        


# Exercicio B

import random

from random import shuffle
def embaralha(nome):
    a = list(nome)
    shuffle(a)
    a = ''.join(a)
    print(a.upper())


nome = input('Digite algo: ')
embaralha(nome)