from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

from ibm_key import get_ibm_key

ibm_key = get_ibm_key("IBM_KEY_LUCAS")

service = QiskitRuntimeService(channel="ibm_quantum", token=ibm_key)

# create circuit
qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.x(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.ccx(qreg_q[2], qreg_q[1], qreg_q[0])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[0], creg_c[2])
circuit.measure(qreg_q[2], creg_c[0])
 
# create backend service and run it
backend = service.backend("ibmq_qasm_simulator")
job = Sampler(backend).run(circuit)

print(f"job id: {job.job_id()}")

result = job.result()

print(result)