#În continuare, vom utiliza quantum computing pentru a genera doi biţi (00, 01, 10, 11). Pentru
#aceasta vom construi un circuit de 2 qubiti, şi vom aplica pe ambii qubiti poarta Hadamard, apoi
#vom măsura şi analiza rezultatele.

import qiskit
import numpy as np
from qiskit import *
from qiskit import QuantumCircuit
from qiskit import Aer
from qiskit.visualization import plot_histogram

circuit = QuantumCircuit(2,2) #creeaza un circuit de 2 qubiti (default in starea |0>) si 2 biti clasici

circuit.h(0) #aplica poarta h pe qubitul 1
circuit.h(1) #aplica poarta h pe qubitul 2
#circuit.measure_all()
circuit.measure([0,1],[0,1]) 
#circuit.measure([a,b],[c,d]) -> masoara qubitul a in bitul clasic c
#                                     si qubitul b in bitul clasic d

print(circuit)
simulator=Aer.get_backend('qasm_simulator')
result=execute(circuit,simulator,shots=8000,memory=True).result()
counts=result.get_counts()
memory=result.get_memory()
print(counts)
#print(memory)
plot_histogram(counts).savefig('histograma.png')
print('----Exercitii----')
print('------Exercitiul8------')

#ex8 a) Construiţi un circuit care acţionează pe un registru de 3 qubiţi.
circuit8=QuantumCircuit(3,3)
#b) Măsuraţi fiecare qubit. Care este rezultatul?
#c) Aplicaţi poarta X asupra primului qubitul. Analizaţi rezultatul.
#d) Afişaţi starea obţinută.

#circuit8.x(0)
circuit8.measure([0,1,2],[0,1,2])
print(circuit8)

simulator8=Aer.get_backend('qasm_simulator')
result=execute(circuit8,simulator8,shots=8000).result()
counts=result.get_counts()
print(counts)


circuit8.x(0)
circuit8.measure([0,1,2],[0,1,2])
print(circuit8)

simulator8=Aer.get_backend('qasm_simulator')
result=execute(circuit8,simulator8,shots=8000).result()
counts=result.get_counts()

print(counts)

print('------Exercitiul9------')
#9. Implementaţi următorul circuit. Reprezentaţi histograma cu rezultatele obţinute.
circuit9=QuantumCircuit(2)
circuit9.h(0)
circuit9.cnot(0,1)
circuit9.x(0)
'''circuit9.i(1)
circuit9.barrier()'''
circuit9.z(0)
circuit9.cnot(1,0)
circuit9.h(1)
circuit9.measure_all()
circuit9.barrier()
print(circuit9)

simulator9=Aer.get_backend('qasm_simulator')
result=execute(circuit9,simulator9,shots=8000).result()
counts=result.get_counts()
print(counts)
plot_histogram(counts).savefig('histograma_ex9.png')

print('------Exercitiul10------')
#10 Implementaţi în Qiskit stările lui Bell β00=1/sqrt(2) (|00>+|11>) și β01=1/sqrt(2) (|01>+|10>)
# Ce obţineţi în urma măsurării în baza computaţională, dar în urma măsurării în baza Bell?

#pentru starea β00=1/sqrt(2) (|00>+|11>)
circuit00=QuantumCircuit(2)
circuit00.h(0)
circuit00.cx(0,1)

#masor in baza computationala circuit00.measure_all()

#masor in baza Bell adica vreu sa masor β00 in baza Bell. pai evident ca probabilitatea o sa dea |β00>
#analogie cu baza computationala psi=|0> -> p(|0>)=1 daca masor in baza computationala;
# daca vreau sa masor in baza lui Hadamard trb sa aflu 0 in funcite de |+> si |-> si |0>=1/sqrt(2) (|+> + |->) 
# adunand starile |+> si |->  
circuit00.barrier()
circuit00.cnot(0,1)
circuit00.h(0)
circuit00.measure_all()
print(circuit00)


simulator00=Aer.get_backend('qasm_simulator')
result=execute(circuit00,simulator00,shots=8000).result()
counts=result.get_counts()
print(counts)
plot_histogram(counts).savefig('histograma_ex10_00.png')

#pentru starea β01=1/sqrt(2) (|01>+|10>)
circuit01=QuantumCircuit(2)
circuit01.x(1)
circuit01.barrier()
circuit01.h(0)
circuit01.cnot(0,1)

#masor in baza computationala circuit01.measure_all()
circuit01.cx(0,1)
circuit01.h(0)
circuit01.measure_all()
print(circuit01)

simulator01=Aer.get_backend('aer_simulator')
result=execute(circuit01,simulator01,shots=8000).result()
counts=result.get_counts()
print(counts)
plot_histogram(counts).savefig('histograma_ex10_01.png')
