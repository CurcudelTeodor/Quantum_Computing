#import matplotlib.pyplot as plt

#alg deutsch
'''
functie constanta sau balansata 
funcite constanta -> oracol simplu de construit
uf|10>  ->  -|10>
ultimul bit e auxiliar
n = 3 -> 4 biti, unul e auxiliar
'''
from qiskit import *
dj=QuantumCircuit(4,3) #,3daca stiu ca masor doar 3 qubiti -> 3 biti clasici
dj.x(3)
dj.barrier()
#pana aici e inputul
for i in range(4):
    dj.h(i)
#+= compun 2 circuite
dj.barrier()
#dj+=balanced_oracle
#print(dj)
dj+=const_oracle #-> obtin 000 deci functia e constanta
dj.barrier()
for i in range(3):
    dj.h(i)
for i in range(3):
    dj.measure(i,i) #masoara qubitul i si pune-l in bitul clasic i
dj.draw()

'''
ca sa nu influenteze starea obtinuta pune not again la sfarsit

'''
#bernstein
'''
3. |-> produs tens |->
are functia widget implentata
mai trebuie sa fac o transformre ca sa ramana minus la -|10>

'''
n=3
bv=QuantumCircuit(n+1,n)
#superpozitie
bv.x(n)
bv.barrier()
for i in range(n+1):
    bv.h(i)
#bv.draw(output='mpl')
#daca nu inversez sirul (secretul) obtin rezultatul pe dos
s='011'
s=s[::-1]
print(s)

bv.barrier()

for i in range(n):
    if s[i]=='0':
        bv.i(i)
    else:
        bv.cx(i,3) #3 adica ultimul
bv.barrier()
for i in range(4):
    bv.h(i)
bv.barrier()
bv.draw(output='mpl')

#ca sa mearga pentru orice secret ar trebui sa generez un secret random 
#dar mereu obtin secretul cu probabilitate 1 

#shor
'''
qubitit canchila -> ajutatori, nu ii masor la final
ii masor inainte sa elimin superpozitia
thus:
doar starile din mijloc le obtin alea care nu au langa ele paranteze
oracol greu de construit -> il import din qiskit simon_oracle

000 * s = 0 
001 * s = 0 -> ne dam seama de ultimul bit (adica primul ca e invers)
...
de la historgrama
-> partea de postprocesare

'''
from qiskit_textbook.tools import simon_oracle
b='11'
sim=QuantumCircuit(2*len(b))
sim.draw()

sim+=simon_oracle(b)
