from random import shuffle
nom1 = input('Digite o nome do(a) aluno(a);  ')
nom2 = input('Digite o nome do(a) aluno(a);  ')
nom3 = input('Digite o nome do(a) aluno(a);  ')
nom4 = input('Digite o nome do(a) aluno(a);  ')
lista = [nom1, nom2, nom3, nom4]
shuffle(lista)
print('A or dos alunos para apresentação é;')
print(lista)