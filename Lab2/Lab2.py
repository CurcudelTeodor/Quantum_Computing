#Crearea de circuite cu qiskit
#import din qiskit
from qiskit import *
from qiskit import Aer
circ=QuantumCircuit(2,2) #-> pun ,2 daca in final voi masura ambii qubiti
#circ.draw() -> nu merge la mine
#circ.draw(initial_state=True)
#nu trb neaparat import matplotlib.pyplot as plt
#circ.draw(output='mpl',filename='wassup.png',initial_state=1)

#plec cu |00>
#aplicarea unei porti de un qubit
circ.h(0)
circ.cx(0,1)
print(circ)

#import matplotlib.pyplot as plt
#circ.draw(output='mpl',filename='wassup.png',initial_state=1)

backend=Aer.get_backend('statevector_simulator')
job=backend.run(circ)
results=job.result()
stare_finala=results.get_statevector(circ,decimals=2)
print(stare_finala)

#plec cu |01>
circ1=QuantumCircuit(2)
circ1.x(1)
circ1.barrier()
circ1.h(0)
circ1.cnot(0,1)
print(circ1)

backend=Aer.get_backend('statevector_simulator')
job=backend.run(circ1)
results=job.result()
stare_finala=results.get_statevector(circ1,decimals=2)
print(stare_finala)

#Matricea asociata circuitului circ (cel care incepe din 00 si ma duce in β00=1/sqrt(2) * (|00> + |11>) 
backend=Aer.get_backend('unitary_simulator')
job=backend.run(circ)
results=job.result()
matrice=results.get_unitary(circ,decimals=2)
print(matrice)

backend=Aer.get_backend('unitary_simulator')
job=backend.run(circ1)
results=job.result()
matrice=results.get_unitary(circ1,decimals=2)
print(matrice)

#Simularea si masurarea circuitului 

#masurare toti qubitii
#circ.measure_all()

#masurare qubitii pe care ii vreau eu
circ.measure(qubit=[0,1],cbit=[0,1])
#circ.measure(0,0) #-> masoara primul qubit si il pune in primul bit
print(circ)

#Ca sa vad ce obtin trebuie sa rulez pe un simulator
backend=Aer.get_backend('qasm_simulator')
job=backend.run(circ,shots=1024) #shots -> de cate ori sa ruleze circuitul
results=job.result() #rezultatul va fi de tip counts, sa vada de cate ori a dat o anumita valoare (adica din 1024 de shoturi, 
#cate au fost pentru fiecare stare de 2 qubiti in cazul asta - am plecat cu 2 qubiti -> imi rezulta 2 qubiti -> principiu mec cuantica parca/ postulate)
counts=results.get_counts()
print(counts) #daca pun measure_all imi da ceva de genu {'00 00': 491, '11 00': 533}
#                                                            |              |  unde am pus barele, aia sunt c_0 si c_1 din circuit (bitii clasici in care nu am masurat nimica)
#afisarea histogramei
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts).savefig('histograma.png')

#from qiskit import IBMQ
#IBMQ.save_account('API')
 
#Exercitii
'''1. a) Construiţi un circuit care acţionează pe un registru de 3 qubiţi.
b) Măsuraţi fiecare qubit. Care este rezultatul? -> ar trebui sa rulez pe un simulator
c) Aplicaţi poarta X asupra primului qubitul. Analizaţi rezultatul.
d) Afişaţi starea obţinută.
'''
#from qiskit_aer import AerSimulator
#AerSimulator().run(circuit).result().get_counts()
circuit = QuantumCircuit(3,1)
circuit.x(0) #000 -> 100 -> de la dreapta la stanga e 001

circuit.measure(0,0)

#circuit.measure_all()
print(circuit)

#rulez pe simulator
backend=Aer.get_backend('qasm_simulator')
job=backend.run(circuit,shots=1024) 
results=job.result()
counts=results.get_counts()
print(counts)

'''2.Implementaţi următoarele circuite
Pentru fiecare dintre circuitele de mai sus, afişati matricea asociată circuitului, vectorul
de stare obţinut după parcurgerea circuitului. Măsuraţi ambii qubiţi şi reprezentaţi histograma cu rezultatele obţinute. 
Dar dacă măsuraţi doar primul qubit al circuitelor, ce rezultate obţineţi?'''

qc=QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
#delimitez entanglement-ul de restul circuitului cu o bariera
qc.barrier()
qc.x(0)
qc.z(0)
qc.cx(1,0)
qc.h(1)
print(qc)

backend=Aer.get_backend('unitary_simulator')
job=backend.run(qc)
results=job.result()
matrice_qc=results.get_unitary(qc,decimals=1)
print(matrice_qc)

backend=Aer.get_backend('statevector_simulator')
job=backend.run(qc)
results=job.result()
stare_finala_qc=results.get_statevector(qc,decimals=1)
print(stare_finala_qc)

qc.barrier()
qc.measure([0,1],[0,1])
#qc.measure(0,0) si sa pun qc=QuantumCircuit(2,1) -> daca vreau sa masor doar primul qubit
print(qc)
backend=Aer.get_backend('qasm_simulator')
job=backend.run(qc,shots=1024) 
results=job.result()
counts=results.get_counts()
print(counts)
plot_histogram(counts).savefig('ex2a.png')

'''chiar daca la statevector imi da ca |00> -> -|11> eu nu pot sa imi dau seama cand masor ca acolo e minus
pentru ca eu iau (amplitudinea in modul)^2 -> modulul imi anuleaza semnul 
'''