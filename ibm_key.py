def get_ibm_key(file : str) -> str:
    f = open(file, "r")
    return f.read()
