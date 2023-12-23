from qiskit_ibm_runtime import QiskitRuntimeService

from ibm_key import get_ibm_key

print(get_ibm_key("IBM_KEY"))

# service = QiskitRuntimeService(channel="ibm_quantum", token="", set_as_default=True)
# service = QiskitRuntimeService()