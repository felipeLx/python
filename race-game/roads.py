class roads:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
    def __str__(self):
        return f"{self.name} is {self.length} km long and {self.width} km wide."