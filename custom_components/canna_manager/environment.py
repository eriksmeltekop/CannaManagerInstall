from homeassistant.helpers.entity import Entity

class TemperatureSensor(Entity):
    def __init__(self, name):
        self._name = name
        self._temperature = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._temperature

    def update(self):
        self._temperature = 25.0