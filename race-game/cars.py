class cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        

    def get_descriptive_name(self):
        long_name = self.make + ' ' + self.model
        return long_name.title()

    def get_model():
        options = ['F1', 'Kart']
        return options