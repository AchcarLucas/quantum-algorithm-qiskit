from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

from ibm_key import get_ibm_key

ibm_key = get_ibm_key("IBM_KEY_LUCAS")

service = QiskitRuntimeService(channel="ibm_quantum", token=ibm_key)

# Create empty circuit
example_circuit = QuantumCircuit(2)
example_circuit.measure_all()
 
# You'll need to specify the credentials when initializing QiskitRuntimeService, if they were not previously saved.
backend = service.backend("ibmq_qasm_simulator")
job = Sampler(backend).run(example_circuit)

print(f"job id: {job.job_id()}")

result = job.result()
print(result)