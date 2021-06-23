class KeyValueStorage:
    """Take a file with key-value pairs, and them take that pairs like self arguments"""

    def __init__(self, path):
        self.path = path
        self.storage = {}
        with open(path) as f:
            for line in f.readlines():
                self.storage[line.split("=")[0]] = line.split("=")[1].rstrip()
        for key, value in self.storage.items():
            if key.isdigit():
                raise ValueError("You cant use int as a key")
            if value.isdigit():
                self.storage[key] = int(value)

    def __getattr__(self, item):
        return self.storage[item]
