from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

from ibm_key import get_ibm_key

ibm_key = get_ibm_key("IBM_KEY_LUCAS")

service = QiskitRuntimeService(channel="ibm_quantum", token=ibm_key)

# create a new circuit with two qubits (first argument) and two classical
# bits (second argument)
qc = QuantumCircuit(2)

# add a Hadamard (H) gate to qubit 0
qc.h(0)

# perform a controlled-X gate (XOR) on qubit 1, controlled by qubit 0
qc.cx(0, 1)

qc.measure_all()

# create backend service and run it
backend = service.backend("ibmq_qasm_simulator")
job = Sampler(backend).run(qc)

print(f"job id: {job.job_id()}")

result = job.result()

print(result)
