"""
race game
pilots: Senna, Piquet, Barriquelo, Fittipaldi and Massa
2 options: kart or f1
2 roads: São Paulo or Rio de Janeiro
"""
class pilots:
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank
    def __str__(self):
        return f"{self.name} is {self.age} years old and is a {self.rank}."

