class robot:
    def __init__(self, name, model):
        self.name=name
        self.model=model
    def a(self, activity):
        return"{} is {}.".format(self.name, activity)
    def m(self, model):
        return"{} is a {} model.".format(self.name, self.model)
r=robot("R2-D2", "Astromech")
print(r.a("beeping"))
print(r.m("Astromech"))