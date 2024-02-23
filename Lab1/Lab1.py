'''import qiskit

print('ez install')'''

n=1
# Afisam numerele de la 1 la 5
while n<=5:
    print(n)
    n=n+1
print("Done")


if n<10:
    print('wassup')
else:
    print("n nu e mai mic de 10")
print("-------------------------------")

a=9
print(type(a))
a=1.5
print(type(a))
a=1-2j
print(type(a))

print("-------------------------------")
a="Hello" 
print(a)
#a[0]='j' eroare: 'str' object does not support item assignment 
#In Python, strings are not mutable, which means they cannot be changed. You can, however, replace the whole variable with the new version of the string.
#https://stackoverflow.com/questions/38601139/str-object-does-not-support-item-assignment-python
a='M'+a[1:]
print(a)
print("---------------------")
lista=['hello',30]

print(lista[0])
lista[0]='altceva'
print(lista[0])

print(lista[1])

print("---------")
lista2=["sir1"]
lista2[0]='sir2'
print(lista2)
print('-----------')

dict = {'Name': 'Ana', 'Age':7, 'Class': 'First','Name':'Teo'}
print("dict['Name']:", dict['Name'])
dict['Age']+=1
print("dict['Age'] dupa modificare:",dict['Age'])
print('---------------------')
print('---------------------')
def suma_none(a,b):
    g=2+2
result=suma_none(1,2)
print(result)

def suma(a,b):
    return a+b
result=suma(1,2)
print(result)
print('---------------------')
import cmath
print(cmath.sqrt(-1))
z=complex(1,-1)
print(z.real,z.imag)
import cmath
print(cmath.e)
print('---------------------')
import random as rand
nr1=rand.randint(1,10) #genereaza un numar intreg din intervalul [1,10]
print(nr1)
nr2=rand.random() #genereaza un numar real (float) din [0,1)
print(nr2)
print('------------Exercitii------------')
#1.Scrieţi un script în Python care afişează toţi multiplii de 3 din intervalul 2 : 50
for i in range(3,50,3):
    print(i)
for i in range(2,50,1):
    if i%3==0:
        print(i)

#2.Scrieţi un script în Python care verifică dacă un număr este par sau nu.
n=101
def par1(n):
    if n%2==0:
        return(1)
    else:
        print('impar')
print(par1(n)) #daca numarul e impar, afiseaza 'impar' si dupa 'None' pentru ca functia nu returneaza nimic in cazul cand n este impar (doar afiseaza)

def par2(n):
    if n%2==0:
        print('par')
    else:
        print('impar')
par2(10)

#6.Realizaţi un script ce calculează adunarea, respectiv înmulţirea a două matrici.
A=[[1,2,3],[3,2,1],[0,0,1]]
print(A)
print("elementul 0 0 este:",A[0][0])
print(len(A)) #len = return the number of items in a container
rezultat=[[0,0,0],[0,0,0],[0,0,0]]

def sumaMatrici(A,B):
    for i in range(len(A)):
        for j in range(len(B)):
            rezultat[i][j]=A[i][j]+B[i][j]
    return(rezultat)

print("suma este:",sumaMatrici(A,A))

'''import numpy as np
print(np.add(A,A))'''
rezultat=[[0,0,0],[0,0,0],[0,0,0]]
rezultat2=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

A=[[1,2,3,4],[3,2,1,1],[0,0,1,9]]
B=[[1,2,3],[3,2,1],[0,0,1],[5,2,1]]

def produsMatrici(A,B):
    rezultat=[[0,0,0],[0,0,0],[0,0,0]]
    if len(A[0]) != len(B):
        return('Matricile nu se pot inmulti!')
    else:
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)): #sau len(A[0]) pt ca sunt egale daca am trecut de if-ul initial care ne zice daca putem sau nu sa inmultim matricile
                    rezultat[i][j]+=A[i][k]*B[k][j]
    return(rezultat)

print("produsul este:",produsMatrici(A,B))
#daca da index out of range probabil matricea rezultat are dimensiunile gresite
B=[[1],[1],[1],[1]]
print("produsul este:",produsMatrici(A,B))

import numpy as np
print(np.matmul(A,B))
print(np.invert(A))
print('----------------------')
X=[[1,0],[0,1]]
print(np.matmul(X,X))
print('---------------------')

from qiskit import QuantumCircuit

circuit = QuantumCircuit(2,2)
circuit.x(0)

circuit.measure_all()
print(circuit)
print('\-\-\-\-\--\-\\-\--\-\-\-\-\\-\-\-')

from qiskit import Aer,transpile
from qiskit.visualization import plot_histogram
from qiskit.tools.visualization import plot_histogram
import qiskit.quantum_info as qi

'''simulator = Aer.get_backend('aer_simulator')
circuit=transpile(circuit,simulator)

result=simulator.run(circuit).result()
counts=result.get_counts(circuit)
'''

cry=QuantumCircuit(2)
cry.h(0)
cry.i(1)
cry.measure_all()
print(cry)


simulator=Aer.get_backend('qasm_simulator')
result=simulator.run(cry,simulator,shots=8000).result()
counts=result.get_counts()
print(counts)
print("Rezultatul simularii este :", counts)
#{'11': 2000, '10': 2002, '00': 2000, '01': 1998}

plot_histogram(counts).savefig('histograma0.png')

print('--------------------')
print('||||||||||||||||||||')
print('--------------------')

