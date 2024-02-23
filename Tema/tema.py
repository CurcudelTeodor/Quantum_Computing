'''Scrieţi o funcţie în Python care având ca input o matrice pătratică A cu elemente
complexe, returnează A†.'''
#convertim din array in matrix ca sa putem folosi sqrt si impartiri
print('\n------------------Exercitiul1------------------\n')
import numpy as np

A=np.array(  [  [1/np.sqrt(2), 2, 4-4j],    [1, 5, +3j],    [2-5j, 1+3j, 6-9j] ]  )
B=np.array(   [   [1, 5, 1-1j, 6-2j], [4, 2+3j, 1j, 2+4j], [9, 4-3j, 1+7j, 3], [8, 10-5j, 4, 9+1j]])

A=np.asmatrix(A)
B=np.asmatrix(B)

def dagger(A):
    Atranspus=A.transpose()
    Adagger=Atranspus.conjugate()
    return(Adagger)
    #return( A.transpose().conjugate() )

print(A,'\n')
print(dagger(A))
print('\n------------------Exercitiul2------------------\n')

'''Scrieţi o funcţie în Python care primeşte ca input trei vectori |a>, |b>, |c> ∈ C^2
şi returnează expresia |ab> <ca|, unde prin |ab> întelegem |a> ⊗ |b>.
'''

'''
Exemplu pentru cazul in care a,b,c nu sunt qubiti:
val1=round(1/np.sqrt(2),2)
val2=round(1/np.sqrt(3),2)

a=np.array([[val1],[-1j]])
b=np.array([[2-1j],[3+1j]])
c=np.array([[5+1j],[val2]])'''

a=np.array([[1],[0]])
b=np.array([[0],[1]])
c=np.array([[0],[1j]])

a=np.asmatrix(a)
b=np.asmatrix(b)
c=np.asmatrix(c)

for i in (a,b,c):
    print(i,'\n')

#<ca| = |ca>†
def ket_ori_bra(a,b,c):
    ket_ab=np.kron(a,b) #produs tensorial
    ket_ca=np.kron(c,a)
    bra_ca=dagger(ket_ca) #folosim functia de mai sus
    rezultat=np.kron(ket_ab,bra_ca)

    return(rezultat)

print('Produsul este:\n',ket_ori_bra(a,b,c))

print('\n------------------Exercitiul3------------------\n')
#a) Scrieţi un program în Python care implementează circuitul de mai sus.
from qiskit import *
circuit3=QuantumCircuit(2)
circuit3.cnot(0,1)
circuit3.h(0)
print(circuit3,'\n')

#b) Asişaţi matricea U ∈ M4(C) asociată circuitului de mai sus şi verificaţi că aceasta
#este unitară (U · U† = U† · U = I4). Pentru a testa egalitatea dintre două matrici A
#şi B, veţi afişa norma || A − B ||. Puteţi utiliza orice normă matriceală implementată în
#biblioteca numpy.

backend=Aer.get_backend('unitary_simulator')
job=backend.run(circuit3)
results=job.result()
U=results.get_unitary(circuit3,decimals=2)

U=np.asmatrix(U) #convertim U la matrice pentru a efectua mai usor inmultirile cu *
print('Matricea U este:\n',U,'\n')
#print(type(U))

produs1=U*dagger(U)
produs2=dagger(U)*U

unu = np.matrix('1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1')
#print(np.trace(unu))
m=produs1-produs2
print('|| UU† - U†U ||=',np.linalg.norm(m))

n=produs1-unu
print('|| UU† - I   ||=',np.linalg.norm(n))

ok=0
#testam daca UU†=U†U
if np.linalg.norm(m)<0.1:
    print('U=U†')
    if np.linalg.norm(n)<0.1:
        ok=1

if ok==1:
    print('Matricea U este unitara\n')
else:
    print('Matricea U NU este unitara\n')

#c) Rulaţi circuitul urmator pe simulatorul ’qasmsimulator’ de 1000 de ori şi afişati rezultatele. Reprezentaţi şi
#histograma corespunzătoare pentru a vizualiza rezultatele.
from qiskit.tools.visualization import plot_histogram

circuit3.measure_all()
print(circuit3)

backend=Aer.get_backend('qasm_simulator')
job=backend.run(circuit3,shots=1000)
results=job.result()
counts=results.get_counts()
print('Rezultatele de la c):',counts,'\n')

plot_histogram(counts).savefig('histograma_ex3c.png')

#d) Verificaţi că circuitul efectuează măsurarea în baza Bell, iniţializând starea de
#input de 2-qubiţi |ψ> cu stările lui Bell |βxy>. Ce rezultate obţineţi şi cu ce probabilitate?

def bell(qubit0,qubit1):
    Bell_circuit=QuantumCircuit(2)

    if qubit0==1 and qubit1==1: #|β11>
        Bell_circuit.x(0)
        Bell_circuit.x(1)
        Bell_circuit.barrier()

    else: 
        if qubit1==1: #|β01>
            Bell_circuit.x(1)
            Bell_circuit.barrier()
        else:
            if qubit0==1: #|β10>
                Bell_circuit.x(0)
                Bell_circuit.barrier()

    #creăm entanglement-ul
    Bell_circuit.h(0)
    Bell_circuit.cx(0,1)
    Bell_circuit.barrier()
    #adaugam circuit3 care face de fapt Decodarea Bell -> de aceea circuitul efectueaza masuratorea in baza Bell
    #input |β00> decodifica ca fiind 00
    circuit_nou=Bell_circuit.compose(circuit3,[0,1])

    return(circuit_nou)
    

circ=bell(0,1) #putem pune si 0,0   1,0    1,1  -> in functie de starea Bell dorita la input
state='01'
print(circ)

#simulam circuitul nou obtinut
backend=Aer.get_backend('qasm_simulator')
job=backend.run(circ,shots=1000)
results=job.result()
counts=results.get_counts()
print(counts)

for key in counts.keys():
    if key[::-1]==state:
        nr=counts.get(key)

probabilitate=nr/1000*100
print('Probabilitatea de a observa' ,state,'este:',probabilitate,'%')

print('\n------------------Exercitiul4------------------\n')
#Scrieţi o funcţie care returnează un circuit cu următoarea matrice unitară. 
#Pentru construirea circuitului utilizaţi doar porţile X, H şi CNOT

def ex4():
    circuit_qiskit=QuantumCircuit(2)
    circuit_qiskit.h(0)
    circuit_qiskit.barrier()
    
    #facem cnot(0,1) cu controlul gol
    circuit_qiskit.x(0)
    circuit_qiskit.cnot(0,1)
    circuit_qiskit.x(0)
    circuit_qiskit.barrier()

    circuit_qiskit.h(1)
    circuit_qiskit.barrier()
    
    circuit_qiskit.x(0)
    print('Circuitul 1')
    print(circuit_qiskit,'\n')

    backend=Aer.get_backend('unitary_simulator')
    job=backend.run(circuit_qiskit)
    results=job.result()
    C=results.get_unitary(circuit_qiskit,decimals=2)
    return(C)

print(ex4(),'\n\n')

#Pentru ca matricea C să arate ca cea de pe foaie, trebuie sa inversăm porțile:
#ce era aplicat pe qubitul 0 se aplică pe qubitul 1 și inversa
def foaie():
    circuit_foaie=QuantumCircuit(2)
    circuit_foaie.h(1)
    circuit_foaie.barrier()

    #cnot cu controlul gol
    circuit_foaie.x(1)
    circuit_foaie.cnot(1,0)
    circuit_foaie.x(1)

    circuit_foaie.barrier()
    circuit_foaie.h(0)
    circuit_foaie.barrier()

    circuit_foaie.x(1)
    print('Circuitul 2')
    print(circuit_foaie,'\n')

    backend=Aer.get_backend('unitary_simulator')
    job=backend.run(circuit_foaie)
    results=job.result()
    C_foaie=results.get_unitary(circuit_foaie,decimals=2)
    return(C_foaie)

print(foaie(),'\n\n')

print('\n------------------Exercitiul5------------------\n')
#Scrieţi o funcţie care având ca input o stare de 2-qubiţi, determină daca qubiţii sunt
#entangled sau nu. Inputul va fi un vector din |ψ> ∈ C4, iar funcţia va returna TRUE dacă
#starea este entangled, respectiv FALSE în caz contrar.

qub1=np.array( [[1/np.sqrt(2)],[0],[0],[1/np.sqrt(2)]] ) #|β00>
qub2=np.array( [[1/2],[1/2],[-1/2],[1/2]])
qub3=np.array( [[1],[0],[0],[0]])

#|ψ><ψ|=ρ_A
#Tr(ρ_A^2) =  1 -> |ψ> separabilă
        #  != 1 -> |ψ> neseparabilă (entangled)

def ex5(qub):
    qub=np.asmatrix(qub)
    qub_dagger=dagger(qub)
    qub_daggger=np.asmatrix(qub_dagger)

    ro=qub*qub_dagger
    ro=np.asmatrix(ro)
    matrice=ro*ro

    rez=np.trace(matrice)
    if rez==1:
        return("starea este separabila\n")
    else:
        return("starea este corelata (entangled)\n")

print(ex5(qub1))
print(ex5(qub2))
print(ex5(qub3))

print('\n------------------Exercitiul6------------------\n')

from math import *

circ6=QuantumCircuit(3,3)

#circ6.initialize([0 ,  1/np.sqrt(3),   1/np.sqrt(3)*(-1/2-1j*np.sqrt(3)/2) ,   0 ,    1/np.sqrt(3)*(-1/2+1j*np.sqrt(3)/2),      0,     0,   0], circ6.qubits)
                #000      100             010                                 110        001                                 101, 011,  111

#circ6.initialize([0,1/np.sqrt(3)*(-1/2+np.sqrt(3)/2.j)*(-1/2+np.sqrt(3)/2.j),1/np.sqrt(3)*(-1/2+np.sqrt(3)/2.j),0,1/np.sqrt(3),0,0,0],circ6.qubits)
#circ6.initialize([0,0,0,0,0,0,0,1])


#circ6.initialize([0,1/np.sqrt(3)*(-1/2+np.sqrt(3)/2.j),1/np.sqrt(3)*(-1/2+np.sqrt(3)/2.j)*(-1/2+np.sqrt(3)/2.j),0,1/np.sqrt(3),0,0,0],circ6.qubits)

#circ.initialize([ 0,1/np.sqrt(3)*(-1/2+np.sqrt(3)/2.j),1/np.sqrt(3)*(-1/2+np.sqrt(3)/2.j)*(-1/2+np.sqrt(3)/2.j),0,1/np.sqrt(3),0,0,0],circ.qubits)

circ=QuantumCircuit(3)
circ.initialize([0,1/np.sqrt(3)*(-1/2+np.sqrt(3)/2.j)*(-1/2+np.sqrt(3)/2.j),1/np.sqrt(3)*(-1/2+np.sqrt(3)/2.j),0,1/np.sqrt(3),0,0,0],circ.qubits)  #psi1
#circ.initialize([ 0,1/np.sqrt(3)*(-1/2+np.sqrt(3)/2.j),1/np.sqrt(3)*(-1/2+np.sqrt(3)/2.j)*(-1/2+np.sqrt(3)/2.j),0,1/np.sqrt(3),0,0,0],circ.qubits) #psi0
def ex6(circ):

    circ.i(0)
    circ.p(2*pi/3,1)
    circ.p(4*pi/3,2)
    circ.x(0)
    
    circ.cnot(0, 1)
    circ.cnot(1, 2)
    circ.ch(0, 1)
    circ.ry(-2 * acos(1 / sqrt(3)), 0)
    circ.measure_all()
    simulator = Aer.get_backend('qasm_simulator')
    job = simulator.run(transpile(circ, backend=simulator), shots=1024)
    result = job.result()
    counts = result.get_counts()
    print(circ)
    print(counts)
    if '000' in counts:
        if(counts['000']==1024):
            return 0
        else:
            return 1 
    else:
        return 1


print(ex6(circ))

#am vrea sa convertim o stare de la inceput in |W> state. De ce? Pentru ca daca aplicam matricea (care ne-a dus in |W>) dagger vom obtine |000>
#|000> -> |W>
#      U 


#psi0 -> |W> -> |000>
#     P      U†  

#psi1 -> |W> -> altceva diferit de |000>
#     P      U†  