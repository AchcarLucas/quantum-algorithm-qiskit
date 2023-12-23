from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

from ibm_key import get_ibm_key

ibm_key = get_ibm_key("IBM_KEY_LUCAS")

service = QiskitRuntimeService(channel="ibm_quantum", token=ibm_key)

# create circuit
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[1])
circuit.id(qreg_q[0])
circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.barrier(qreg_q[0])
circuit.barrier(qreg_q[1])
circuit.id(qreg_q[1])
circuit.id(qreg_q[0])
circuit.barrier(qreg_q[1])
circuit.barrier(qreg_q[0])
circuit.h(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
 
# create backend service and run it
backend = service.backend("ibmq_qasm_simulator")
job = Sampler(backend).run(circuit)

print(f"job id: {job.job_id()}")

result = job.result()

print(result)