import json

class  PetExport:
    def export(self, dog):
        raise NotImplementedError

class ExportJSON:
    def export(self, dog):
        return json.dumps({
            "name": dog.name,
            "breed": dog.breed,
        })

class ExportXML:
    def export(self, dog):
        return

class Pet:
    def__init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed = None):
        super().__init__(name)
        self.breed = breed

class ExDog(Dog):
    def__init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed=None)
        self._exporter = exporter

    def export(self):
        return self._exporter.export(self)

dog = ExDog("Шарик", "Дворняга", exporter=ExportXML())
print(dog.export)

    