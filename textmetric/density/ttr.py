def measure(text):
    if not text.strip():
        raise ValueError
    tokens = text.split()
    types = set(tokens)
    return len(types) / len(tokens)
